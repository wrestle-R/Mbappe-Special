---
name: tagged-release
description: Prepare and carry out an authorized tagged release, with Sol owning publication and repairs and Luna
  handling supported passive waits. Use when asked to release, publish a version or create a release tag; ordinary
  edits and commits do not trigger publication.
---

# Tagged Release

Sol owns implementation, verification, release creation and repairs. Luna owns the passive wait. A model handoff is an orchestration action, never something a Markdown file can perform by itself.

## Prepare

Read the repository release workflow. Establish the target commit, tag, artifact, required checks and publication authorization. Do not equate a pushed tag with a successful release. Record the exact run IDs, repository, commit SHA and expected artifacts. Preserve signing material and existing tags.

## Hand off the wait

Discover the orchestrator capabilities before delegating. Use the available Sol model for implementation and the user-requested Luna model for monitoring. Resolve real model identifiers from capabilities; never guess a model alias or silently substitute a different model. If Luna or automatic return-to-Sol is unavailable, report the limitation before promising the handoff.

Start one Luna delegate scoped to the exact release run. Give it the run IDs, SHA, expected artifact names and a finite monitoring deadline. Luna may read status and logs; it must not edit, retry, retag, publish, merge or change settings. Use event-driven wait mechanisms supplied by the host, follow their continuation instructions, and avoid polling loops. If host rules reserve PR watching for the parent, keep that watcher in the parent; do not delegate it to Luna.

Return terminal success, failure, cancellation or timeout to Sol through the host-supported completion mechanism. Include run links, final status, artifact evidence and a concise failure excerpt with secrets removed. Cancel obsolete delegates.

## Finish or repair

Sol verifies the terminal report and artifact identity. On failure, diagnose and fix the cause, run relevant checks, and retry only within existing authorization. Allow at most two automatic repair attempts per release unless the user sets another limit. Never overwrite a published tag or duplicate a release to hide a failure. Stop with evidence when credentials, external configuration or a new consequential decision is required.

Report the release link, commit and artifact checks. Distinguish a validated skill from an actual successful model handoff. A timeout is incomplete, never success.
