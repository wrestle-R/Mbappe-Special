# Pstack catalog review

Catalog screened from the pinned backnotprop/pstack revision in upstream-sources.json. Included means copied unchanged into this collection. Conditional means useful for a specific task but deferred. The remaining entries overlap existing guidance or add more process than the routine workflow needs.

| Skill | Decision | Purpose |
| --- | --- | --- |
| architect | Conditional, deferred | Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in |
| arena | Conditional, deferred | Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it |
| automate-me | Deferred, overlap or specialized process | Use for "automate me", "create/update/refresh my -mode skill", "turn/capture my preferences or working style into a skill", or wanting agents to follow how the user works |
| benchmark-checklist | Conditional, deferred | Vet a perf measurement (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it |
| blast-radius | Conditional, deferred | Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up |
| bro | Deferred, overlap or specialized process | Restate the last message in plain human language, with no jargon. |
| correct | Included | Find the mistakes agents keep repeating in this repo and make each one impossible |
| create-formal-verification-skill | Conditional, deferred | Generate a project-local skill that formally verifies the code where a bug costs the most and tests reach the least, in any language, with whichever verification tool fits |
| create-verification-skill | Conditional, deferred | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform |
| figure-it-out | Deferred, overlap or specialized process | Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away |
| how | Conditional, deferred | Use for "how does X work", code walkthroughs before changing something, and placement / ownership / layering questions ("where should this live", "which package owns this", "is this the righ |
| in-your-own-words | Included | Restate in your own words what you think the user's goals are and what problem they're trying to solve |
| interrogate | Conditional, deferred | Use for "interrogate", "adversarial review", "multi-model review", "challenge this", "stress test this code", "find blind spots", or "tear this apart" |
| ketchup | Deferred, overlap or specialized process | Catch the user up on what changed in this chat since their last message, in plain words and small visuals |
| ketchup-video | Deferred, overlap or specialized process | Catch the user up like /ketchup, with a short subtitled video of slides for what happened and the waiting calls as text under it |
| maintain-formal-verification-skill | Conditional, deferred | Bring a project's formal verification back in line with the code after the code changes: find the commits that touched verified code, update the model, harness, or properties to describe the |
| maintain-verification-skill | Conditional, deferred | Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of proven correcti |
| make-bot-ui | Deferred, overlap or specialized process | Build a bot-facing UI. |
| no-comments | Conditional, deferred | Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints. |
| poteto-help | Deferred, overlap or specialized process | Guides users through pstack setup, /poteto-mode, and picking the skill, playbook, or principle for a task |
| poteto-mode | Deferred, overlap or specialized process | poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work |
| principle-attack-the-premise | Deferred, overlap or specialized process | Apply when two or more fixes that share one premise have failed the same gate |
| principle-boundary-discipline | Deferred, overlap or specialized process | Apply when wiring validation, error handling, or framework adapters |
| principle-build-the-lever | Deferred, overlap or specialized process | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks |
| principle-encode-lessons-in-structure | Deferred, overlap or specialized process | Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction |
| principle-exhaust-the-design-space | Deferred, overlap or specialized process | Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase |
| principle-experience-first | Deferred, overlap or specialized process | Apply when product, UX, or feature-scope tradeoffs come up |
| principle-explain-the-number | Deferred, overlap or specialized process | Apply before you measure, and before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result |
| principle-fix-root-causes | Included | Apply when debugging |
| principle-foundational-thinking | Deferred, overlap or specialized process | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share |
| principle-guard-the-context-window | Deferred, overlap or specialized process | Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning |
| principle-laziness-protocol | Deferred, overlap or specialized process | Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading |
| principle-make-operations-idempotent | Included | Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries |
| principle-migrate-callers-then-delete-legacy-apis | Deferred, overlap or specialized process | Apply when introducing a new internal API while old callers still exist |
| principle-minimize-reader-load | Deferred, overlap or specialized process | Apply when reviewing or shaping code that's hard to trace |
| principle-model-the-domain | Deferred, overlap or specialized process | Apply when writing stateful logic, or when code branches a lot or repeats a shape assumption across files. |
| principle-never-block-on-the-human | Deferred, overlap or specialized process | Apply when tempted to ask 'should I do X?' on reversible work. |
| principle-outcome-oriented-execution | Deferred, overlap or specialized process | Apply during planned rewrites and migrations with explicit phase boundaries |
| principle-prove-it-works | Included | Apply after completing a task, before declaring done |
| principle-redesign-from-first-principles | Deferred, overlap or specialized process | Apply when integrating a new requirement into an existing design. |
| principle-separate-before-serializing-shared-state | Deferred, overlap or specialized process | Apply when concurrent actors might write to the same file, branch, key, or state object |
| principle-sequence-verifiable-units | Deferred, overlap or specialized process | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs |
| principle-subtract-before-you-add | Deferred, overlap or specialized process | Apply when sequencing an addition, refactor, or rewrite |
| principle-test-behavior-not-implementation | Included | Apply when you write, change, or keep a test |
| principle-type-system-discipline | Deferred, overlap or specialized process | Apply when designing types, reviewing a function signature, or writing code in any statically-typed language |
| recall | Deferred, overlap or specialized process | Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state brief |
| reflect | Deferred, overlap or specialized process | Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill |
| setup-pstack | Deferred, overlap or specialized process | Configure which models pstack uses per role and at what reasoning budget |
| sharpen | Included | Make a task deeper, not bigger, then rewrite the prompt |
| show-me-your-work | Conditional, deferred | Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result) |
| statechart | Conditional, deferred | Check a TLA+ model of a system that moves between states, such as a product flow, a protocol, or a service, and draw it as a Mermaid statechart |
| swarm | Conditional, deferred | Fan out N parallel workers, drain them, and return one report |
| tdd | Included | Use only when the user explicitly asks for TDD, a failing test, or a regression test, OR when the bug has an obvious cheap local test target |
| teach | Conditional, deferred | Explain a body of work plainly so a person actually understands it |
| technical-writing | Deferred, overlap or specialized process | Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax |
| typescript-best-practices | Conditional, deferred | TypeScript best practices |
| unslop | Included | Cut AI tells from any writing. |
| why | Included | Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds |
