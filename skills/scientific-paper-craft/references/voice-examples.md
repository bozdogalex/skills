# Voice examples

The examples below are fictional teaching material, not quotations or findings
from a manuscript. They illustrate writing decisions rather than facts to copy
into a paper. Apply a proposed revision only when the underlying evidence
supports it.

## Connect related ideas without producing fragments

Before: "The sampling frame covers urban parks. The interviews examine visitors'
experiences."

After: "We interviewed visitors to the urban parks in the sampling frame to
understand how they experienced these spaces."

Keep the connection only when the context supports it. Short sentences remain
useful for definitions, emphasis, and independent findings.

## Explain the problem before introducing the mechanism

Before: "We introduce an uncertainty-aware adaptive acquisition mechanism."

After: "A fixed sampling schedule can miss short changes in water quality.
Our method samples more frequently when uncertainty about the current
measurement increases."

The explanation establishes the purpose; later sections define the uncertainty
measure, sampling rule and assumptions. It does not by itself establish that
the method detects more events.

## Make the conclusion about completed work

Before: "Further validation is needed. Future work should investigate the
method in more settings."

After: "We compared two segmentation methods on the same annotated images.
The results identify the boundary types on which their errors differed."

Use such wording only when those results exist. Move detailed future work to
Discussion and state reproduction limitations once where they affect claims.

## Explain scope without erasing important limitations

Before: "The survey identifies preferences; it does not establish causation."

After: "The survey characterizes respondents' preferences at the time of data
collection. We interpret differences between groups as associations."

Keep the explicit causal limitation where it constrains the research question
or interpretation. Positive wording must not conceal a design limitation.

## Match formalization to the algorithm

For an iterative numerical method, define the input, update rule, convergence
criterion and iteration limit. If the source specifies only a tolerance, label
any proposed iteration cap as an additional assumption, not an implemented
feature. For a distributed operation, distinguish an attempted write from a
confirmed write and an external reply; name only the persistence and atomicity
properties established by the source. A formal-looking operation name does not
establish those guarantees. Use a prose example when it clarifies the sequence.

## First-use terminology

Prefer "the proportion of reference-positive samples detected by the test
(sensitivity)" to an unexplained specialist abbreviation when writing for a
broader scientific readership. Distinguish similarly named measurements where
confusion changes interpretation. Define field-specific terms without adding
an encyclopedic glossary of concepts the intended reader already knows.
