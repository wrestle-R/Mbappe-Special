---
name: rdp-commit
description: Use when writing or revising Git commit messages for Russel.
metadata:
  version: 1.0.0
---

# RDP Commit

Use this skill when naming a Git commit for Russel.

## Write the subject

- Inspect the staged diff and describe the real change in a few ordinary words.
- Keep it short, casual, and usually lowercase. A fragment is fine: `made the readme clearer` or `auth is working finallyyy`.
- Prefer the natural name of the thing over polished verbs or a summary of architectural significance.
- Mix plain subjects with occasional lingo, relief, or humor when it fits. Do not make every commit a joke or reuse the examples unless they accurately describe the change.
- Skip `feat:`, `fix:`, `chore:`, scopes, and ticket numbers unless the repository requires them.
- Do not claim tests passed or work shipped unless the evidence supports it. Add a body only when the change needs context or the user asks.
- Follow any required format in the repository, even when it differs from the usual style.

## Final check

Would Russel say this naturally, and does it name what changed? If it sounds like release notes, shorten it. Do not change Git author identity or repository configuration to affect commit style.
