# Skill descriptions: before and after

This document compares the parsed YAML `description` values in the 24 skill files at baseline `00f7c3b043be07c306dd4cb86b4fe1e0a2e9cddc` and updated commit `d81f77f39414c17dd35128e48bf30d6e764c9934`.

## anthropic

### frontend-design

Source: [`skills/anthropic/frontend-design/SKILL.md`](../skills/anthropic/frontend-design/SKILL.md)

**Before:**

> Lead visual design for application UI, dashboards, interactive tools and components, or when Anthropic frontend-design is requested. Also use for websites when selected as the design lead. Do not compete with a selected design-taste-frontend lead; preserve the approved project theme.

**After:**

> Use for app UI, dashboards and components, or when Anthropic frontend-design is selected for a website.

## leonxlnx

### design-taste-frontend

Source: [`skills/leonxlnx/design-taste-frontend/SKILL.md`](../skills/leonxlnx/design-taste-frontend/SKILL.md)

**Before:**

> Lead visual design for a new or redesigned marketing, company, product or portfolio website when no design lead is selected, or when asked for taste or to fix a generic AI-looking page. Use its website art direction and tooling; reuse the approved theme and do not compete with a selected frontend-design lead.

**After:**

> Use for marketing, product, company or portfolio website design, or when taste is requested.

## mattpocock

### diagnosing-bugs

Source: [`skills/mattpocock/diagnosing-bugs/SKILL.md`](../skills/mattpocock/diagnosing-bugs/SKILL.md)

**Before:**

> Diagnose and fix reported bugs, crashes, broken behaviour, failing checks or performance regressions. Use for normal requests such as fix this, debug this, this is broken or this is slow. Reproduce the actual symptom and verify the fix.

**After:**

> Use when asked to fix, debug or diagnose broken behaviour, crashes, failing checks or performance regressions.

### grilling

Source: [`skills/mattpocock/grilling/SKILL.md`](../skills/mattpocock/grilling/SKILL.md)

**Before:**

> Clarify a consequential feature idea, plan or product decision before implementation. Use when asked to plan, ideate, stress-test an idea or ask the important questions, or when material scope choices remain open. Skip settled decisions and routine reversible details.

**After:**

> Use when planning a feature, clarifying consequential decisions, stress-testing an idea or asking pre-implementation questions.

### setup-matt-pocock-skills

Source: [`skills/mattpocock/setup-matt-pocock-skills/SKILL.md`](../skills/mattpocock/setup-matt-pocock-skills/SKILL.md)

**Before:**

> Configure project tracker and domain documentation when first using the spec or ticket workflow and that configuration is missing, or when asked to change that setup. Reuse existing configuration; do not run setup on every task.

**After:**

> Use when project tracker configuration is missing for the spec/ticket workflow, or when asked to change it.

### to-spec

Source: [`skills/mattpocock/to-spec/SKILL.md`](../skills/mattpocock/to-spec/SKILL.md)

**Before:**

> Turn settled feature decisions or an approved planning conversation into a specification. Use when asked to write a spec or PRD, or at the specification stage of the approved feature workflow. Do not restart the interview; publishing follows the configured tracker and task authorization.

**After:**

> Use when asked for a spec or PRD, or when settled feature decisions need a specification.

### to-tickets

Source: [`skills/mattpocock/to-tickets/SKILL.md`](../skills/mattpocock/to-tickets/SKILL.md)

**Before:**

> Break an agreed specification or plan into complete implementation tickets with blockers and acceptance criteria. Use when asked for tickets, issues or a work breakdown, or after the feature spec is settled. Review the breakdown before publishing it.

**After:**

> Use when breaking an agreed spec or plan into implementation tickets, issues or a work breakdown.

## pstack

### correct

Source: [`skills/pstack/correct/SKILL.md`](../skills/pstack/correct/SKILL.md)

**Before:**

> Prevent a demonstrated recurring class of agent or code mistakes. Use when the user says this keeps happening, stop repeating this mistake or asks to make a rule enforceable. Confirm repetition from evidence; do not treat every isolated correction as a repository-wide refactor.

**After:**

> Use when asked to prevent recurring agent mistakes or enforce a repeatedly missed requirement.

### in-your-own-words

Source: [`skills/pstack/in-your-own-words/SKILL.md`](../skills/pstack/in-your-own-words/SKILL.md)

**Before:**

> Restate the user’s intended outcome when asked what you understood, to explain the request back, or to confirm a complex ambiguous brief before proceeding. Keep the restatement short; skip it for clear routine requests.

**After:**

> Use when asked to restate a request or confirm understanding of a complex brief.

### principle-fix-root-causes

Source: [`skills/pstack/principle-fix-root-causes/SKILL.md`](../skills/pstack/principle-fix-root-causes/SKILL.md)

**Before:**

> Apply while debugging or fixing broken behaviour: trace the symptom to the first incorrect state or decision and fix it there. Use alongside diagnosing-bugs; avoid symptom-only guards and retries that hide the fault.

**After:**

> Use while debugging or fixing broken behaviour to trace the underlying fault.

### principle-make-operations-idempotent

Source: [`skills/pstack/principle-make-operations-idempotent/SKILL.md`](../skills/pstack/principle-make-operations-idempotent/SKILL.md)

**Before:**

> Apply when implementing retries, offline queues, sync, installation commands or lifecycle operations that can run more than once or resume after interruption. Make repeated execution converge safely without duplicate effects.

**After:**

> Use when implementing retries, offline queues, sync, installers or operations that may run repeatedly.

### principle-prove-it-works

Source: [`skills/pstack/principle-prove-it-works/SKILL.md`](../skills/pstack/principle-prove-it-works/SKILL.md)

**Before:**

> Apply when finishing implementation, a bug fix, a build, an installation or a release, before reporting completion. Verify the actual changed behaviour or artifact and state anything that remains unverified.

**After:**

> Use before reporting completion of implementation, fixes, builds, installations or releases.

### principle-test-behavior-not-implementation

Source: [`skills/pstack/principle-test-behavior-not-implementation/SKILL.md`](../skills/pstack/principle-test-behavior-not-implementation/SKILL.md)

**Before:**

> Apply when writing, editing or reviewing tests. Assert observable behaviour and useful invariants so tests catch broken behaviour while surviving internal refactors. Does not require adding tests to every change.

**After:**

> Use when writing, changing or reviewing tests.

### sharpen

Source: [`skills/pstack/sharpen/SKILL.md`](../skills/pstack/sharpen/SKILL.md)

**Before:**

> Improve or rewrite a task prompt when asked to make it clearer, more precise or more rigorous without expanding scope. Use for sharpen this prompt or improve this brief. Do not replace an ordinary implementation request with a prompt-writing exercise.

**After:**

> Use when asked to improve, clarify or sharpen a task prompt or brief.

### tdd

Source: [`skills/pstack/tdd/SKILL.md`](../skills/pstack/tdd/SKILL.md)

**Before:**

> Add a focused failing-before test for a bug fix when requested, or when there is an obvious cheap local regression-test target. Use for TDD and regression-test requests; do not force broad test infrastructure for a small fix.

**After:**

> Use for TDD or regression-test requests, or bug fixes with an obvious cheap local test target.

### unslop

Source: [`skills/pstack/unslop/SKILL.md`](../skills/pstack/unslop/SKILL.md)

**Before:**

> Write or edit assistant chat replies, explanations, status updates and technical prose addressed to Russel in plain language without AI writing patterns. Apply to ordinary replies; use russelore instead for blogs, website copy and other text written as Russel.

**After:**

> Use for assistant replies, explanations, status updates and technical prose addressed to Russel.

### why

Source: [`skills/pstack/why/SKILL.md`](../skills/pstack/why/SKILL.md)

**Before:**

> Explain why a project decision was made, why a design exists or what led to a regression, using commits and discussions as evidence. Use for project rationale and history questions, not generic runtime walkthroughs.

**After:**

> Use when asked why a project decision was made, why a design exists or what led to a regression.

## russel

### eyes-of-render

Source: [`skills/russel/eyes-of-render/SKILL.md`](../skills/russel/eyes-of-render/SKILL.md)

**Before:**

> Coordinate Russel’s normal feature, app and UI requests, from planning through implementation and verification. Use for building or changing a feature, website, native app or widget; route to relevant specialist skills and skip unnecessary stages for small clear changes. Also use when asked to wake or resume the owner’s existing InstaBox.

**After:**

> Use for feature, app, website or widget work, UI consistency checks, or requests to wake the owner’s InstaBox.

### half-send

Source: [`skills/russel/half-send/SKILL.md`](../skills/russel/half-send/SKILL.md)

**Before:**

> Complete approved work autonomously when Russel says half-send, asks you to finish while he is away, or approves implementation after planning. Gather remaining material decisions once, reuse settled answers, then execute the approved scope.

**After:**

> Use when Russel says half-send, asks for work while away, or approves implementation after planning.

### rdp-commit

Source: [`skills/russel/rdp-commit/SKILL.md`](../skills/russel/rdp-commit/SKILL.md)

**Before:**

> Name or revise a Git commit when committing authorized changes for Russel. Inspect the diff and write a short casual subject. This skill names commits; it does not authorize creating or pushing them.

**After:**

> Use when writing or revising Git commit messages for Russel.

### readme-rdp

Source: [`skills/russel/readme-rdp/SKILL.md`](../skills/russel/readme-rdp/SKILL.md)

**Before:**

> Create, rewrite, simplify or improve a project README for Russel. Use for README requests; compose owner-authored prose with russelore and follow his requested contents and layout.

**After:**

> Use when creating, rewriting, simplifying or improving a project README.

### russelore

Source: [`skills/russel/russelore/SKILL.md`](../skills/russel/russelore/SKILL.md)

**Before:**

> Write or edit text as Russel: blogs, website copy, portfolio copy, captions and personal README prose. Use when drafting in his voice or editing his words; ordinary assistant explanations use unslop, and commit subjects use rdp-commit.

**After:**

> Use when writing blogs, website copy, captions or other text as Russel, or editing his drafts.

### skeuomorphism-ui

Source: [`skills/russel/skeuomorphism-ui/SKILL.md`](../skills/russel/skeuomorphism-ui/SKILL.md)

**Before:**

> Install and compose Gavin’s Skeuomorphism UI React components, or build matching tactile additions. Use when Russel asks for skeuomorphic UI, raised keys, recessed fields, physical controls, or this skeuomorphism-lib registry. Read the host project before installing; preserve an explicitly chosen different library and do not use for generic 3D artwork.

**After:**

> Use for Gavin’s Skeuomorphism UI library, skeuomorphic React interfaces, raised keys, recessed fields or matching tactile components.

### tagged-release

Source: [`skills/russel/tagged-release/SKILL.md`](../skills/russel/tagged-release/SKILL.md)

**Before:**

> Prepare and carry out an authorized tagged release, with Sol owning publication and repairs and Luna handling supported passive waits. Use when asked to release, publish a version or create a release tag; ordinary edits and commits do not trigger publication.

**After:**

> Use when asked to create a tagged release or publish a version.
