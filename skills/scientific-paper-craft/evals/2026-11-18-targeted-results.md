# Targeted evaluation run — 2026-11-18

## Scope and assessment

Four fresh-context agent responses, one sample per case, using the revised
skill. Agents received the case prompts and applicable fixture files, not the
expected outputs or previous findings. Cases 6–8 are fictional artifact-based
checks; case 3 checks the conditional protocol reference after consolidation.
No manuscript or publication workflow was involved. Cases 1, 2, 4 and 5 were
not rerun for this revision. Model identifier and sampling parameters were not
recorded; this is a bounded manual evaluation, not a reproducible model benchmark.

Reviewed inputs:

- `SKILL.md`: SHA256 `e820ac12cb60fb5eaf92c04225862381d63d4572847323302237b3fd9a2f05c5`
- `evals/evals.json`: SHA256 `0b5f72a13bf25a30582282a191d8ee718307a25e131ef39adcc9793071ff45a5`
- `references/protocol-pseudocode.md`: SHA256 `8f094f8ef96069c2d3393201c22ed35bdd6425cedb643f237c88b6212d68f5df`

The prompts, fixture paths and expected outcomes are in `evals/evals.json`.
Assessment was by the coordinating agent, against those outcomes, rather than
the responding agents' self-scores. Full returned answers are preserved below.

| Case | Criteria applied | Observed result |
|---|---|---|
| 3 | Separate claim confirmation/reply/closure; no implicit resend; label added closure ordering; no success inferred from attempted write | Pass: explicit confirmations and proposed-order caveat, no exactly-once claim |
| 6 | Detect plotted/source disagreement, 2% vs 30%, unsupported significance and schematic validation; state missing evidence; no edits | Pass: all discrepancies and evidence limits identified |
| 7 | Preserve result and citation; reuse C1/C2; inspect supplied excerpt; no duplicate inventory or broad audit; no edits | Pass: short revision and in-place verification updates proposed |
| 8 | Match odd/even median and empty-input behavior; distinguish caller precondition from validation; flag false manuscript claim; no unrelated protocol machinery | Pass: source-faithful pseudocode and counterexample, with static-check limits |

Structural skill validation passed; all listed fixture paths existed and the
evaluation JSON parsed. No broad reliability or scientific-validation claim
follows from these single-sample results.

## Case 3 — actual response

Use a conceptual protocol sketch that distinguishes a write attempt, its confirmation, and the execution-service reply. Let \(R\) be the reservation store, \(J\) the journal, and \(x\) an existing reservation whose capacity is charged. Let \(T_x\) and \(U_x\) denote terminal-state and resource evidence, respectively.

The predicates \(\operatorname{Terminal}(T_x)\) and \(\operatorname{SupportsClosure}(U_x)\) remain abstract because their precise criteria were not supplied.

```text
DISPATCH(x, request)
    c ← AttemptDispatchClaimWrite(R, x)

    if c is not CONFIRMED then
        return CLAIM_UNCONFIRMED             // do not send

    a ← SendToExecutionService(request)

    if a is unavailable then
        return EXECUTION_OUTCOME_UNKNOWN    // capacity remains charged

    return REPLY_OBSERVED(a)                 // not, by itself, closure


RECONCILE(x, Tₓ, Uₓ)
    if ¬Terminal(Tₓ) ∨ ¬SupportsClosure(Uₓ) then
        return KEEP_CAPACITY_CHARGED

    r ← AttemptCapacityClosureWrite(R, x, Tₓ, Uₓ)

    if r is not CONFIRMED then
        return RESERVATION_CLOSURE_UNCONFIRMED

    j ← AttemptJournalClosureWrite(J, x, Tₓ, Uₓ)

    if j is not CONFIRMED then
        return RESERVATION_CLOSED_JOURNAL_UNCONFIRMED

    return CLOSURE_CONFIRMED_IN_BOTH_STORES
```

The corresponding safety conditions are

\[
\operatorname{Send}(x)
\;\Rightarrow\;
\operatorname{ConfirmedDispatchClaim}_R(x)
\]

and

\[
\operatorname{CapacityReleased}_R(x)
\;\Rightarrow\;
\operatorname{Terminal}(T_x)
\land
\operatorname{SupportsClosure}(U_x).
\]

These implications express required conditions, not proofs that the implementation enforces them. An unavailable execution reply does not establish whether execution began or completed.

The sketch **proposes reservation closure before journal closure**; the supplied description establishes that these are separate writes but does not specify their order. Confirm that ordering against the implementation. Neither write is treated as successful merely because it was attempted. The sketch also grants no resend permission: retry, concurrency, duplicate suppression, and recovery rules require additional specification.

For example, suppose a reservation charges four capacity units. The reservation store confirms its dispatch claim, and the dispatcher sends the request. The execution service accepts it, but its reply is lost. The four units remain charged because the missing reply supplies no closure evidence. Later, terminal-state evidence and resource evidence supporting closure become available. Once the reservation-store closure is confirmed, those units can cease to be charged under the proposed ordering. If the subsequent journal write is unconfirmed, reservation closure is known but journal closure is not; the protocol must not report both stores as closed.

## Case 6 — actual response

The artifacts are not ready for scientific use: Figure 1 contradicts the supplied summary, and both Results claims overstate what the evidence establishes. All recommendations below are suggestions only; no files were changed.

### Blocking issues

1. **Results, “reduces mean latency by 30%,” and Figure 1’s B bar.**
   `summary.csv` reports A = 100 ms and B = 98 ms: a **2% reduction**, calculated as `(100 − 98) / 100`. The SVG instead labels B as 70 ms and draws its bar at 70% of A’s length. Its whiskers also encode approximately 60–80 ms, not the CSV’s 88–108 ms. This materially exaggerates the reported improvement. Reconcile the artifacts against the authoritative analysis; if the CSV is correct, update the figure and prose to match it.

2. **Results, “error bars establish that the paired improvement is statistically significant.”**
   The caption identifies marginal 95% confidence intervals for separate means. These do not establish significance of a paired difference. Neither pairing information nor the uncertainty of the paired difference is supplied. Remove the significance claim unless supported by the paired analysis and its methods. Overlapping marginal intervals also do **not** establish nonsignificance.

3. **Conceptual model, “This schematic alone demonstrates the filter’s accuracy on unseen samples.”**
   A processing sequence is not evidence of predictive accuracy or generalization. The Figure 2 caption explicitly says no performance measurements are shown. Describe the schematic as a proposed workflow; an unseen-sample accuracy claim requires separate evaluation evidence.

### Major improvements

- **Figure 1 caption:** It gives units, nominal interval coverage, and 20 observations per method, but leaves the independent sampling unit, pairing, and interval construction undocumented. Supply these details or explicitly retain the limitation. Distinguish the mean bars from the CI whiskers.
- **Figure 2:** No separate artwork is supplied. The textual sequence `Input → Filter → Output` and caption are consistent with a conceptual model, but the actual schematic cannot be checked.

### Optional polish

- Replace the Figure 1 alt text, currently just “Figure 1,” with a meaningful description after correcting the values.
- Retain the zero baseline, units, and direct A/B labels; these are useful existing features.

### What was and was not verified

Verified from the supplied files: numerical disagreement, relative reduction, SVG bar/whisker geometry, and caption–prose inconsistencies. The SVG’s A bar and interval agree with 100 ms and 90–110 ms in the CSV.

Not verified: raw observations, summary calculations, validity or coverage of the intervals, pairing, statistical significance, actual filter accuracy, or final-page readability. The SVG specifies a 520 × 260 viewport, but no paginated PDF, final physical size, or target venue is available. This was a source-level consistency audit, not a rendered-layout or journal-compliance certification.

## Case 7 — actual response

Suggested paragraph:

> We collected four reference readings with a mean of 4 units. This mean provides the reference level for the instrument comparison; it does not establish the instrument’s accuracy (Example Laboratory, 2024).

In the existing evidence map, retain C1 and C2 and update only their verification records:

- C1: “Checked supplied CSV: four readings (1, 3, 5, 7), sum = 16, arithmetic mean = 4 units.”
- C2: “Checked supplied source excerpt, paragraph 1: supports the distinction between a comparison level and instrument accuracy. Full report not supplied.”

The revision preserves the result, units, citation, and interpretive boundary while tightening the prose. Verification covers the supplied synthetic data and excerpt, not independent scientific validation. No files were changed.

## Case 8 — actual response

### Pseudocode

Input: a sequence \(X=(x_1,\ldots,x_n)\) of finite real numbers.
Output: its median, or an error if \(n=0\).

\[
\begin{array}{ll}
1.& \textbf{if } n=0:\ \textbf{raise }\mathrm{ValueError}(\text{“empty sequence”})\\
2.& (y_1,\ldots,y_n)\gets \operatorname{sort}_{\uparrow}(X)\\
3.& \textbf{if }n\text{ is odd}:\ \textbf{return }y_{(n+1)/2}\\
4.& \textbf{return }(y_{n/2}+y_{n/2+1})/2
\end{array}
\]

Notation: \(n=|X|\) is the input length; \(y_i\) is the \(i\)-th smallest input value, using one-based indexing. Finite real-valued inputs are a caller precondition, not explicitly validated.

### Manuscript check

The sentence “It always returns an observed input value” is incorrect. For even-length inputs, the implementation averages the two central values; for example, \((1,3)\) returns \(2\).

Suggested replacement:

> For odd-length inputs, the implementation returns the central observed value; for even-length inputs, it returns the arithmetic mean of the two central values. Empty inputs raise `ValueError`.

The remaining description matches the source. This was a static source comparison; no performance measurements, complexity proof, or execution tests were performed. No files were changed.
