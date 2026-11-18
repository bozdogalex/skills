# Stateful and distributed algorithm sketches

Use only for algorithms whose scientific interpretation depends on state,
concurrency or failures. Follow the actual specification or implementation;
keep unspecified operations abstract. Identify stores, relevant state/version
boundaries and required evidence. Separate supplied behavior from proposed
assumptions and label additions where they are used, especially durability,
atomicity, acknowledgements, retries and release ordering.

An attempted write, a confirmed state change and an external service reply are
different outcomes. A helper name such as `ReleaseOnce` does not establish
atomic or exactly-once behavior. Advance only on the confirmation required by
the supplied contract; do not report successful closure merely because a write
was attempted. Preserve defined failure-stop and no-resend boundaries without
inventing recovery permissions.

Show separate writes as separate steps rather than implying a cross-store
transaction. State any assumption needed to justify a chosen ordering or
guarantee; if the evidence does not resolve it, identify the gap. Retain a prose
worked example when it helps readers distinguish these events. A conceptual
sketch is not implementation verification or a proof of distributed execution
semantics.
