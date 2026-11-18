---
name: scientific-paper-craft
description: Draft, revise, or assess scientific manuscripts for coherent argument, evidence-bound claims, natural scholarly voice, and study-design-appropriate reporting. Use for manuscript prose, related work, captions, algorithms where relevant, and readiness reviews; not for general copywriting or conducting new studies.
---

# Scientific Paper Craft

Write for a scientifically literate reader in the paper's intended discipline
who may not specialize in its particular research problem. Match the author's
approved voice and the target venue's conventions without sacrificing technical
precision.

**Adapt to the research design.** Before substantive drafting, identify the
discipline, study type, intended readership, and applicable methodological or
reporting standards. Use appropriate supporting skills or verified guidelines
to apply field-specific conventions and inferential standards. Preserve the
underlying evidence. Apply computational experiments, algorithms, hypothesis
tests and software-reproducibility requirements only where the research design
calls for them.

## Establish the task and venue

1. Identify the supplied text or exact source and, when relevant and available,
   the current PDF, requested scope, and mode: suggestions only, authorized edits,
   or readiness assessment. In suggestions-only mode,
   leave the manuscript, bibliography, and packages unchanged.
2. Resolve the venue and article type from the current request and reliable
   project context. Ask if absent or ambiguous; do not silently inherit a venue
   from an unrelated earlier paper. For venue-independent prose work, offer to
   proceed provisionally rather than blocking on venue selection.
   For whole-paper drafting and submission-readiness assessments, identify
   applicable reporting standards and relevant extensions using
   [references/reporting-standards.md](references/reporting-standards.md).
   Record its scope and verified version, or explain why none applies; a
   checklist supports complete reporting, not proof of methodological validity.
   For focused prose edits, preserve existing reporting conventions without
   repeating a full standards audit unless the change materially affects
   study reporting.
3. For whole-paper preparation, a venue change, or submission-readiness work,
   read [references/venue-study.md](references/venue-study.md). It covers the
   official author/authorship rules and ten recent comparable articles. Reuse
   an existing verified study when appropriate. A focused sentence edit does
   not require repeating that research.
4. Use approved author samples to establish voice. Consult
   [references/voice-examples.md](references/voice-examples.md) for generic
   techniques when useful; these fictional examples do not establish the
   current author's preferences.

## Build the scientific argument

Before substantive drafting, identify the research problem, closest established
work, evidence-supported contribution, practical or theoretical consequence,
and limitations. Distinguish proposed mechanisms from what was actually studied;
record gaps instead of inventing evidence. Frame validation of established
methods as benchmarking, synthesis or empirical characterization rather than
methodological invention. For focused edits, inspect only enough context to
preserve the existing argument.

An abstract should let an outsider identify the setting and practical problem,
what existing approaches establish, the contribution, and the principal findings
or theoretical result, as appropriate. Lead with what the work contributes and
teaches; retain important negative findings and distinguish proposals from
tested or established results.
Use the venue's actual abstract constraints, not a universal one-page rule.

Choose section order for the research story. Combine or separate Discussion
and Threats to Validity as the work and venue justify. Keep the conclusion
about what the study established and learned; put substantial future
research plans in Discussion. Do not force an experimental outline on a
theoretical, qualitative, design-science, or experience-report paper.

## Write connected, precise prose

- Explain specialist terms where first needed, usually in a short apposition.
  Define local abbreviations before use and explain symbols beside equations.
  An abstract must work independently of definitions in the body. Explain
  domain assumptions rather than explaining the intended reader's basic knowledge.
- Use active voice and past tense for what the authors did, and present tense
  for system behavior, definitions, and what figures show. Passive voice is
  appropriate when the actor is immaterial; consistency concerns meaning,
  not a ban on a grammatical construction.
- Give each paragraph a clear role and connect its sentences by cause,
  contrast, or consequence. Combine related short statements when that helps
  flow; split overloaded sentences. Avoid mechanical sentence-length targets.
- Prefer concrete actions and named mechanisms to promotional adjectives,
  vague importance claims, and synonym swapping. Recast gratuitous em-dashes
  with ordinary punctuation when useful, without disturbing technical notation.
- State the evidence positively where possible. Retain negation that defines
  safety boundaries, exclusions, uncertainty, or what a result cannot establish.
  Place a caveat where it changes interpretation; trim repetitions elsewhere.
- Compare related work by the dimensions material to the contribution, such as
  mechanism, assumptions, population, context, theory or evaluation scope.
  Explain the closest differences instead of listing titles
  or asserting that competing work lacks a feature without checking it.

## Protect the scientific meaning

Preserve numerical results, units, signs, denominators, intervals, comparisons,
citations, assumptions, qualitative meanings and study dispositions. Flag
suspected errors separately instead of silently repairing them during a style
pass. Keep pilot, calibration,
confirmatory, engineering, and held-out evidence distinguishable where relevant.
A successful technical check is not automatically evidence of scientific efficacy.

**Evidence traceability.** For whole-paper drafting and substantive revisions,
maintain a claim-to-evidence map outside the manuscript. Reuse and update an
existing verified map when available rather than creating competing evidence
inventories. Link major empirical statements to original data or artifacts,
relevant statistical quantities
(including units, denominators and uncertainty), analysis conditions, and
supporting references. For qualitative or theoretical claims, trace the
interpretive materials or premises and derivations appropriate to the design.
Record missing or inaccessible evidence explicitly. Distinguish numerical
verification from independent scientific validation: internally generated
summaries are derived evidence, not independent confirmation of the underlying
study or implementation.

**Citation integrity.** Distinguish sources actually inspected from references
inherited from earlier drafts or secondary summaries. Verify that each cited
source within the review scope supports the specific claim attributed to it.
For focused edits, check affected attributions and reuse verified records for
unchanged claims. For whole-paper assessments, state which claims and sources
were checked and which remain unverified. A relevant title or abstract
alone is insufficient. Inspect the primary source at the depth needed to check
the claim. When access is unavailable, flag the attribution as unverified and
report the limitation; do not invent bibliographic metadata or imply inspection.

**Reproducible provenance.** For repository-backed manuscript work, use Git to
version manuscript sources, analysis scripts and artifact manifests; identify
the revision reviewed or packaged and any uncommitted differences. For standalone
or externally supplied manuscripts, preserve the source revision or document
identity where available and explicitly report provenance limitations. Modify
a repository or create commits only when authorized by the current task;
read-only review does not grant that authorization.
Keep sensitive or oversized data out of Git and trace them through manifests
and appropriate storage. For shareable research outputs, strongly recommend a
versioned archival deposit such as Zenodo or an appropriate disciplinary
repository, respecting consent, privacy and access restrictions. Distinguish a
reserved DOI or draft from a published deposit; creating repositories,
uploading and publishing still
require task-specific authorization.

**Algorithms and pseudocode.** Include pseudocode when it improves understanding
of the contribution or is explicitly requested. Define inputs, outputs,
assumptions, notation and relevant decision logic. Match detail to the algorithm
and research design; describe state, concurrency or failure behavior where
scientifically relevant. Verify against the implementation or specification,
distinguish conceptual steps from implemented behavior, and label added
assumptions. Formal notation must not imply an unproven guarantee. For stateful
or distributed algorithms, read
[references/protocol-pseudocode.md](references/protocol-pseudocode.md).

**Figures and tables.** Treat each visual as part of the scientific argument.
Verify that data-bearing figures faithfully represent the underlying evidence
and uncertainty, and that conceptual diagrams accurately reflect the described
model. Give each figure a clear purpose, self-contained caption and appropriate
discussion in the text. Review axes, units, legends, tables, layout and
rendered-page readability. Distinguish conceptual illustrations from empirical
validation and report unavailable verification evidence. Use
`scientific-visualization` for figure creation or substantial redesign rather
than duplicating its detailed guidance; preserve existing artwork unless
changes are authorized. Include table cells, footnotes and algorithm notes in
the prose review.

## Use supporting skills selectively

Discover installed skills and read the relevant skill fully before using it.
These are capability names, not hardcoded paths or mandatory dependencies:

| Need in the current task | Supporting skill |
|---|---|
| Argument and section flow | research-paper-writing, when its disciplinary scope fits |
| Voice and readability | academic-humanizer |
| Citation metadata, links, published successors | citation-management |
| Evidence, design, or claim validity | scientific-critical-thinking; peer-review for a requested structured assessment |
| Scientific figure design or inspection | scientific-visualization |
| Rendered document and source-package checks | pdf:pdf or the document-format skill |
| Venue-specific requirements | venue-templates plus the official current guide |
| Study-design reporting | peer-review or relevant domain skill plus verified reporting guidelines |

Use only the capabilities needed, not the entire table. If one is unavailable,
use a transparent bounded fallback. Resolve conflicts in favor of the current
user request and evidence: avoid automatic sentence chopping, citation padding,
or changing meaning to satisfy a checklist. Keep AI-use disclosure accurate;
this workflow improves writing rather than concealing assistance.

## Verify authorized edits

For authorized edits, compare changed text with the prior version. Check that
results and citations remain intact; inspect exceptions such as explicitly
requested reference corrections. Rebuild with existing project scripts where
applicable, or export through the document's established workflow. Render
affected pages and verify cross-references, notation, figure/table readability,
and package manifests. Copy a proofreading PDF only when requested and verify
its identity against the intended build. Distinguish completed checks from
unavailable ones; a successful export or build is not scientific or venue acceptance.

## Report a manuscript review

For manuscript reviews, group findings by scientific consequence:

- **Blocking issues:** incorrect scientific claims, unsupported conclusions,
  invalid citations, or material methodological ambiguity.
- **Major improvements:** unclear contribution, weak research narrative,
  missing comparison, or insufficient explanation of an important result.
- **Optional polish:** style, transitions, formatting, or caption readability.

For each issue, give its location (page/section and a short identifying passage),
problem, scientific consequence, recommended correction, and authorization
status (authorized within current scope, suggestions only, or needs approval).
Calibrate severity to the actual claim and evidence; a missing comparison is
not automatically grounds for a new experiment. Separate confirmed defects
from questions requiring unavailable evidence. State when a level has no
findings, summarize the checks and their limits, and give a clear readiness
judgment. Do not invent findings to justify another pass.

## Stop and hand off

Prefer the smallest revision that materially improves scientific clarity,
correctness or publication readiness. Once the argument, evidence and
presentation meet the requested standard, stop polishing rather than generating
another round of stylistic alternatives.

Stop when the requested scope is addressed, scientific invariants hold, the
requested artifacts verify, and remaining issues have been disclosed. Do not
run new studies, contact coauthors, upload confidential text to external tools,
publish artifacts, send messages, or submit manuscripts without task-specific
authorization. Search public source metadata, not unpublished manuscript text.

In the handoff, summarize substantive edits and checks, identify unresolved
author decisions, and link the exact deliverables. Keep audit scaffolds outside
the manuscript. Never claim review, approval, or testing that did not occur.
