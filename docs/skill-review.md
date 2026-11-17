# Skills that fit this workflow

The collection keeps upstream skills under their authors, with their original names and licenses, and customized automatic-selection metadata. The installer can discover the nested layout because every skill is grouped, including the owner’s skills under `skills/russel/`. Install one by its frontmatter name, such as `--skill diagnosing-bugs`.

## The default flow

For a new feature, use grilling → to-spec → to-tickets → half-send. Configure the tracker once with setup-matt-pocock-skills. Grilling asks decision questions in numbered rounds with recommended MCQ answers. The spec records the agreed outcome. Tickets divide it into complete verifiable slices with blockers. Half-send carries the approved work through implementation without restarting settled questions.

For UI, settle a visual direction before the full build. Choose taste or Anthropic frontend-design as the lead, then use eyes-of-render throughout implementation to keep the approved theme, density, controls and resizing consistent. Verify the actual app or widget when native behaviour matters.

For bugs, use diagnosing-bugs and principle-fix-root-causes. Reproduce the reported symptom, find the cause and rerun the same check after the fix. Use tdd where a focused regression test is practical. Finish with principle-prove-it-works.

For writing, use russelore for website copy, blogs, README prose and other text written as the owner. Use unslop for assistant chat replies and explanations to the owner. Do not flatten the owner’s raw writing into unslop’s sentence rules.

Commit each meaningful verified milestone using rdp-commit. For an authorized release, use tagged-release and readme-rdp, checking the real downloads and installed version. A release, deployment or push still follows the current task’s authorization.

This is the owner’s approved default routing. Installing a helper does not require invoking it on every task. Small clear changes can skip the planning chain.

## Selected pstack skills

| Skill | Why keep it |
| --- | --- |
| [unslop](../skills/pstack/unslop/SKILL.md) | Plain assistant replies without AI writing patterns. |
| [sharpen](../skills/pstack/sharpen/SKILL.md) | Improve an ambitious prompt without enlarging its scope. |
| [in-your-own-words](../skills/pstack/in-your-own-words/SKILL.md) | Check the agent understood a tangled request before it acts. |
| [why](../skills/pstack/why/SKILL.md) | Explain prior decisions from commits and discussions instead of guessing. |
| [correct](../skills/pstack/correct/SKILL.md) | Turn repeated implementation mistakes into enforceable fixes when explicitly invoked. |
| [tdd](../skills/pstack/tdd/SKILL.md) | A practical failing-before regression check when the test path is clear. |
| [principle-fix-root-causes](../skills/pstack/principle-fix-root-causes/SKILL.md) | Avoid the repeated cycle of symptom fixes. |
| [principle-prove-it-works](../skills/pstack/principle-prove-it-works/SKILL.md) | Verify actual behaviour and artifacts before calling work done. |
| [principle-test-behavior-not-implementation](../skills/pstack/principle-test-behavior-not-implementation/SKILL.md) | Keep tests tied to what users and callers observe. |
| [principle-make-operations-idempotent](../skills/pstack/principle-make-operations-idempotent/SKILL.md) | Useful for offline queues, retries, installers and sync operations. |

All 58 pstack catalog entries were screened. The selected instructions were read before inclusion. [The inventory](pstack-review.md) records a decision for every entry. This is a curated selection rather than a copy of pstack’s entire operating style.

## Keep the heavier tools optional

Arena, swarm, architect and interrogate depend on deliberate model orchestration and can consume substantial time. They are useful when independent alternatives or review are explicitly wanted, but need host and model configuration before promising a handoff.

Recall and reflect overlap the owner’s durable memory workflow. Their upstream procedures introduce additional delegation and review stages. Keep the existing private local-docs continuity for routine work; consider these tools for a dedicated history or workflow review.

Poteto-mode changes the agent’s overall working style, while russelore, half-send and eyes-of-render already express the owner’s preferences. Do not install it as a competing default. Technical-writing and bro also overlap the confirmed writing split.

Formal verification and statechart tools suit difficult state invariants rather than every small app change. Benchmark-checklist is a useful later addition when performance comparisons become a regular task.

## Other installed skills

Use shadcn and next-best-practices when that project uses them. Use web-design-guidelines for an accessibility review, redesign-existing-projects for a broad redesign, and image-to-code when a visual reference should lead implementation. Use stitch-design-taste only for Google Stitch DESIGN.md work; it is a different tool from Leonxlnx’s taste skill.

The bklit skills were removed from the installed collection at the owner’s request. No bklit skills belong in this repo. Bklit-specific pr-open and unit-tests guidance should not become universal workflow requirements for unrelated projects.

The review used all 21 other top-level threads accessible through this environment’s thread listing, including one fork with inherited overlap. It paged through their available user messages. Deleted threads, unavailable environments and inaccessible older sessions are outside that coverage. No private transcript or credential values belong in this shared review.
