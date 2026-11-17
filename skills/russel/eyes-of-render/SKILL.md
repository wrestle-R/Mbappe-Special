---
name: eyes-of-render
description: Apply Russel’s repository organisation and visual consistency preferences when implementing or reviewing UI across web, apps and widgets.
---

# Eyes of Render

Keep the root easy to read. Group substantial platform implementations under clear names such as `next/`, `kotlin/` or `tauri/`; create only folders the project uses. Keep required root configuration where its tools expect it. Inspect imports, builds and deployment paths before moving existing code.

## Writing and local access

Use russelore for website copy, blogs, README prose and other text written as Russel. Use pstack’s unslop for assistant chat replies and explanatory text addressed to him. Do not automatically apply unslop’s punctuation and fragment rules to his authored voice. Exact commands, identifiers and facts stay exact.

Before asking where access is configured, read the target project’s instructions and private local notes. In the owner’s local Mbappe-Special checkout, private credentials are kept under `/home/rdp/Desktop/code/Mbappe-Special/secrets/`, ignored by Git. On another machine, discover its actual configured location; do not assume the same path or sync this directory. Locate only the credential needed for the authorized task. Never print values, copy them into documentation, commit them, or treat storage as permission to use them. Ask before every use of a stored sudo password. Use the host’s secret-entry tool if a missing credential is required.

Real project environment files stay ignored and are synced through Vathavaran / Varte after authorized edits, using file paths and the confirmed repository/directory/environment destination. Read CLI help; report confirmed success or a specific pending blocker without values. Example files with placeholders do not need upload.

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
