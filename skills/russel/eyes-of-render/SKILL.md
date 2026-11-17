---
name: eyes-of-render
description: Coordinate Russel’s normal feature, app and UI requests, from planning through implementation and verification.
  Use for building or changing a feature, website, native app or widget; route to relevant specialist skills and
  skip unnecessary stages for small clear changes.
---

# Eyes of Render

Keep the root easy to read. Group substantial platform implementations under clear names such as `next/`, `kotlin/` or `tauri/`; create only folders the project uses. Keep required root configuration where its tools expect it. Inspect imports, builds and deployment paths before moving existing code.

## Writing and local access

Use russelore for website copy, blogs, README prose and other text written as Russel. Use pstack’s unslop for assistant chat replies and explanatory text addressed to him. Do not automatically apply unslop’s punctuation and fragment rules to his authored voice. Exact commands, identifiers and facts stay exact.

Before asking where access is configured, read the target project’s instructions and private local notes. In the owner’s local Mbappe-Special checkout, private credentials are kept under `/home/rdp/Desktop/code/Mbappe-Special/secrets/`, ignored by Git. On another machine, discover its actual configured location; do not assume the same path or sync this directory. Locate only the credential needed for the authorized task. Never print values, copy them into documentation, commit them, or treat storage as permission to use them. Ask before every use of a stored sudo password. Use the host’s secret-entry tool if a missing credential is required.

Real project environment files stay ignored and are synced through Vathavaran / Varte after authorized edits, using file paths and the confirmed repository/directory/environment destination. Read CLI help; report confirmed success or a specific pending blocker without values. Example files with placeholders do not need upload.

## Select only the skills this task needs

Read the installed skills’ descriptions and select by the actual request. Companion names refer to installed skills, not just folders in this source repository. Load their instructions before using them. If one is unavailable, report the material gap and use existing equivalent project artifacts rather than inventing a successful invocation.

For a substantial feature with unresolved decisions, use grilling, then to-spec once settled, then to-tickets once the spec is agreed, then half-send for approved execution. These are stages, not four interviews. Do not begin implementation during requested planning-only work. A clear small edit can proceed directly to the relevant specialist and verification.

For a marketing, product or portfolio website, default to design-taste-frontend. For app UI, dashboards and components, default to frontend-design. An explicit user choice or established design lead wins. Use eyes-of-render for implementation consistency with either lead; do not load both design leads by default.

For ordinary assistant replies, use unslop. For text authored as Russel, use russelore. Use readme-rdp for README structure and rdp-commit for commit subjects. An explicit request for a particular voice wins. For testing, retries and completion checks, load the matching pstack principle only when that operation is part of the task. Correct, sharpen and in-your-own-words apply to their specific requests, not every task.

When code review is requested or required, use gpt-6-luna in a dedicated T3 delegate_task with role review on the current enabled Codex provider. Leave the coding model unchanged. Each review or re-check is a fresh read-only review task; report unavailable Luna rather than substituting. This does not add a review to every task.

## Default workflow

For feature work, use grilling → to-spec → to-tickets → half-send. Reuse decisions already settled in the conversation and skip unnecessary planning stages for a small clear change. Use numbered MCQ question rounds with recommended answers when decisions remain open. Confirm intake is complete before implementation; the approved spec and ticket set carry forward as the execution brief.

For UI work, settle the direction with taste or Anthropic frontend-design before the full implementation. Choose one design lead, then use this skill to check implementation against that direction throughout the ticket work.

For bugs, use diagnosing-bugs: diagnose → reproduce → fix → prove. Make the reported symptom observable, test the cause, and rerun the original check after the fix. Use the selected pstack root-cause and verification principles when useful; add a focused regression test when practical.

Commit meaningful verified milestones using rdp-commit when committing is authorized. Tagged-release applies only when a release is authorized; do not infer publication or deployment from implementation approval.

## From questions to implementation

Use `grilling` to settle the important decisions, `to-spec` to capture the agreed outcome, and `to-tickets` to split it into verifiable work with explicit blockers. Configure Matt Pocock’s tracker integration with `setup-matt-pocock-skills` before those publishing steps. Then use `half-send` for autonomous implementation of the approved ticket set. Reuse settled answers; do not restart the interview. Each skill is optional and separately installable, so read existing equivalent specs or tickets when companions are absent.

For frontend work, select a design lead with the user’s brief: `design-taste-frontend` for its website art direction and tooling, or Anthropic’s `frontend-design` for a distinct visual direction. Both can be installed, but choose one lead per task and borrow only compatible guidance from the other. User instructions and the approved project theme take precedence. Use `stitch-design-taste` specifically for Google Stitch DESIGN.md work, rather than treating it as the general taste skill. Use image-to-code when the task calls for a generated visual reference before coding. Do not require every design skill on every UI change.

Keep the layout compact where the task calls for it. Avoid oversized empty headers and padding, preserve readable spacing and comfortable touch targets, and check vertical as well as horizontal resizing.

## Carry the theme through

Identify the project’s approved theme and tokens before styling. Share colour roles, typography, spacing and corner treatment across the website, app and widgets, adapting to native constraints. Shadcn is a web component system; translate its visual tokens to native UI rather than promising identical components.

Theme every surface, including dropdowns, menus, tooltips, dialogs, checkboxes, radio buttons, disabled states and focus rings. Check text and icons against their actual backgrounds, including gradients and selected states. Do not use colour as the only indication of completion or error.

Icon-only actions need theme-matched tooltips and accessible names. Keep drag reordering on a clear handle rather than a separate Move button. Do not hide essential instructions in a tooltip or let a long-press tooltip consume a drag gesture.

Native defaults are not evidence of a matching theme. Inspect the actual dialog, input, option menu and checkbox surfaces; replace platform accent colours, uppercase actions and default panel shapes when they clash. Use real system-bar insets instead of guessed top padding. Signed-in dashboards should put the user’s activities before promotional copy.

## Inspect the result

Before presenting implementation as finished, inspect narrow, middle and wide layouts. For heatmaps, resize both the container and the cell grid; check gaps and cell bounds rather than assuming a fixed height works with aspect ratios. Rebuild or reload the actual running app after changes so evidence matches the current source.

Exercise the changed controls and inspect the rendered UI at relevant sizes and both themes. Check loading, empty, error, offline, long-label and large-text states. For widgets, verify minimum and expanded sizes, launcher resizing, tap targets, app-opening routes and logging actions on a real supported device when available. A browser concept is not proof of native behaviour.

Keep a short evidence checklist with what was viewed, exercised and still unverified. Fix observed defects before calling the work polished. Never claim perfect or universal behaviour from one screenshot or one device.
