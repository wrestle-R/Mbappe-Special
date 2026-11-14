---
name: eyes-of-render
description: Apply Russel’s repository organisation and visual consistency preferences when implementing or reviewing UI across web, apps and widgets.
---

# Eyes of Render

Keep the root easy to read. Group substantial platform implementations under clear names such as `next/`, `kotlin/` or `tauri/`; create only folders the project uses. Keep required root configuration where its tools expect it. Inspect imports, builds and deployment paths before moving existing code.

## Carry the theme through

Identify the project’s approved theme and tokens before styling. Share colour roles, typography, spacing and corner treatment across the website, app and widgets, adapting to native constraints. Shadcn is a web component system; translate its visual tokens to native UI rather than promising identical components.

Theme every surface, including dropdowns, menus, tooltips, dialogs, checkboxes, radio buttons, disabled states and focus rings. Check text and icons against their actual backgrounds, including gradients and selected states. Do not use colour as the only indication of completion or error.

Icon-only actions need theme-matched tooltips and accessible names. Keep drag reordering on a clear handle rather than a separate Move button. Do not hide essential instructions in a tooltip or let a long-press tooltip consume a drag gesture.

Native defaults are not evidence of a matching theme. Inspect the actual dialog, input, option menu and checkbox surfaces; replace platform accent colours, uppercase actions and default panel shapes when they clash. Use real system-bar insets instead of guessed top padding. Signed-in dashboards should put the user’s activities before promotional copy.

## Inspect the result

Before presenting implementation as finished, inspect narrow, middle and wide layouts. For heatmaps, resize both the container and the cell grid; check gaps and cell bounds rather than assuming a fixed height works with aspect ratios. Rebuild or reload the actual running app after changes so evidence matches the current source.

Exercise the changed controls and inspect the rendered UI at relevant sizes and both themes. Check loading, empty, error, offline, long-label and large-text states. For widgets, verify minimum and expanded sizes, launcher resizing, tap targets, app-opening routes and logging actions on a real supported device when available. A browser concept is not proof of native behaviour.

Keep a short evidence checklist with what was viewed, exercised and still unverified. Fix observed defects before calling the work polished. Never claim perfect or universal behaviour from one screenshot or one device.
