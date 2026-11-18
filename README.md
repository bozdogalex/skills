# Skills

Reusable agent skills for evidence-bound scientific writing and review.

## Available skills

| Skill | Purpose |
|---|---|
| [scientific-paper-craft](skills/scientific-paper-craft/SKILL.md) | Draft, revise and review scientific manuscripts while preserving evidence, adapting to the research design, and keeping claims within their support. |

## Installation

With Node.js and npm available, use the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add bozdogalex/skills --skill scientific-paper-craft -g
```

Select your agent when prompted. `-g` installs at user scope; omit it for a
project-level installation. To target Codex explicitly:

```sh
npx skills add bozdogalex/skills --skill scientific-paper-craft -g -a codex
```

Inspect available skills without installing:

```sh
npx skills add bozdogalex/skills --list
```

Update an installed copy:

```sh
npx skills update scientific-paper-craft
```

The skill is a directory of instructions and references, not an npm package or
an executable manuscript processor. `npx` runs the installer; this repository
supplies the skill. Consult the CLI's current documentation for runtime
requirements and supported agents. Review skill contents before installing.

## Usage

In an agent that supports explicit skill invocation, for example Codex:

```text
Use $scientific-paper-craft to review this manuscript for its intended
readership and research design. Report suggestions only; do not change files.
```

For an authorized revision:

```text
Use $scientific-paper-craft to clarify the Results section. Preserve all
numbers, citations, assumptions and limitations. Change only the supplied
source; do not send, upload or submit anything.
```

Supply the manuscript, target venue if known, requested scope, and available
supporting evidence. Approved writing samples can establish author voice;
the bundled fictional examples illustrate techniques rather than personal style.

The skill covers contribution and argument, claim-to-evidence traceability,
citation integrity, research-design reporting, figures and tables, algorithms
where relevant, and structured manuscript reviews. It distinguishes blocking
issues, major improvements and optional polish.

## Supporting skills and limitations

This is an orchestrating writing skill, not a substitute for disciplinary
expertise, primary-source verification, statistical validation, author consent
or peer review. It cannot establish the correctness of unavailable data or
guarantee publication readiness or acceptance.

It can route specialized work to separately installed capabilities such as
`academic-humanizer`, `citation-management`, `scientific-critical-thinking`,
`peer-review`, `scientific-visualization`, `research-paper-writing`,
`venue-templates` and PDF/document tools. Those skills are not bundled or
installed automatically; availability, names and disciplinary scope vary by
agent. Missing capabilities must be disclosed and handled with a bounded fallback.

Repository changes, commits, uploads, messages and submission actions still
require authorization. A review request does not authorize those actions.
Protect confidential manuscript and participant data when choosing tools.

## Evaluation

[Nine cases](skills/scientific-paper-craft/evals/evals.json) cover claim
calibration, venue/authorship boundaries, protocol assumptions, qualitative
reporting, clinical prediction and citation checks, visual evidence consistency,
reuse of an evidence map, a stateless numerical algorithm, and adaptation of
the four-move abstract structure to theoretical results and venue constraints.

[The recorded targeted run](skills/scientific-paper-craft/evals/2026-11-18-targeted-results.md)
preserves actual responses and manual scoring criteria for cases 3, 6, 7 and 8.
All four passed that run. The other cases were not run in that recorded revision.
These are single-sample behavioral checks, not a comprehensive reliability
benchmark or independent scientific validation. All bundled manuscript and
data fixtures are fictional.

## Contributing

Keep each skill self-contained under `skills/<name>/`, with a `SKILL.md` entry
point and only the supporting resources it needs. Propose changes with a
concrete use case, preserve authorization boundaries, and add or update a
focused evaluation when behavior changes. Do not include confidential research,
credentials or unlicensed third-party materials.

## License

[MIT](LICENSE), copyright 2026 Alex Bozdog. Linked third-party tools, skills
and guidelines remain subject to their own licenses and terms.
