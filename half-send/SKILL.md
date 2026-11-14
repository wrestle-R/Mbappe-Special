---
name: half-send
description: Trigger when the user says “half-send.” Check local preferences and past lessons, ask task-critical questions and get approval before starting, then complete the approved task autonomously.
---

# Half Send

The user invokes this when they expect to go away and cannot answer follow-up questions. Treat it as an intake phase followed by an autonomous execution phase. Do not start task-changing work until the user has answered the intake and approved the execution brief. Keep reusable preferences and lessons in the current workspace's `local-docs/`; these are local-only and must never be committed or pushed.

## 1. Inspect and prepare the intake

Use the task and available context to understand the likely work. Read relevant project instructions and inspect the workspace read-only when that will help make the questions concrete. Before drafting questions, read `local-docs/half-send-preferences.md` and `local-docs/half-send-events.md` if they exist; apply relevant preferences and turn relevant past misses into explicit questions or checks in this task's intake. Do not edit files, run commands with side effects, contact people, or mutate external services during intake.

Think through the task as if you had to finish it without another reply. Work through the likely paths to completion and identify decisions that could change the result, acceptance criteria, scope boundaries, constraints, dependencies, likely blockers, proof, and consequential actions. Ask up front about every material unknown that could force a pause or materially change the outcome. Cover plausible approaches and edge cases when they matter to this task; do not ask about far-fetched possibilities or details with an obvious, reversible default.

The intake should cover, when relevant:

- What outcome should count as done, and which details matter most?
- What scope, constraints, compatibility requirements, or preferences should guide the work?
- What likely decisions can be safely made with defaults, and what must be confirmed?
- Which actions are authorized: edits, tests, commits, branch or PR creation, force-push of this task's branch, merge, deployment, publication, data changes, or external communication?
- What should happen if a required check fails, a dependency is unavailable, or the task cannot be completed safely?

Tailor the questions to the actual task. Aim for complete coverage, not the fewest questions: combine related decisions into clear groups, explain why consequential choices matter, and recommend a sensible default for each. Do not ask the user to decide routine implementation details. Use the harness's question/input mechanism so the conversation visibly waits for the user's answers; do not rely on a normal message that can be mistaken for task completion.

If a material decision is already clear from the user's request or project instructions, do not ask it again. Never request credentials in chat; use the approved secret-entry mechanism if a secret is genuinely needed.

## 2. Confirm the execution brief

After the user answers, summarize the goal, acceptance criteria, scope, assumptions/defaults, proof to collect, and exact side effects they authorized. Ask for a clear go-ahead before starting. If their answer to the intake already explicitly approves that summarized plan, treat that as the go-ahead and proceed without a redundant approval round.

If the user does not approve, revise the brief or stop. Approval applies only to the described task and actions. It does not bypass system, harness, repository, or platform permissions and approval gates.

## 3. Events (local learning log)

When the user points out a missed requirement, preference, risk, or likely decision—or you discover that an important task-specific question should have been asked before execution—capture the reusable lesson in `local-docs/half-send-events.md`. Keep entries short and useful for future intake: date, what was missed, the corrected guidance, and what to ask or check next time. Do not include secrets or unnecessary personal/task details. If a preference is clearly reusable across tasks, also add it to `local-docs/half-send-preferences.md`.

On every later invocation, read these local files before asking questions and turn applicable lessons into pre-execution questions or checks. Do not wait until implementation to surface them. Preserve older entries so the skill can continue learning.

These files are private working notes. Never stage, commit, push, publish, or copy their contents into GitHub issues, pull requests, or other external services. Keep repository ignore rules for them. Update and push the skill, README, and other requested shareable files as authorized, while leaving the local notes out of GitHub.

When the user requests a change to this skill, update the repository copy at `half-send/SKILL.md` and the installed account copy at `$CODEX_HOME/skills/half-send/SKILL.md`, then commit and push the shareable repository changes to its configured GitHub remote. Stage only the files intended for GitHub. Never stage or change `local-docs/half-send-events.md` as part of a skill update; leave the events log local and unstaged. If the remote or authentication is unavailable, finish the local changes and report what is needed to push.

## 4. Execute autonomously

After approval, complete the approved task end to end. Do not ask routine questions or send progress pings that require a reply. Make reasonable, reversible decisions within the approved scope and note material assumptions in the final report. Keep the work focused on the requested outcome and preserve unrelated user changes.

For software changes, use the repository's instructions and workflow. Work from a clean, appropriate branch when needed; implement the smallest complete change; run the relevant checks authorized in the brief; inspect the resulting diff; and report concrete proof. Create, monitor, or merge a PR only if that action was included in the approved brief. If PR monitoring can wake the thread when something changes, use the repository or harness's supported watcher rather than a tight polling loop.

Never infer authorization for production changes, deployment, publication, deleting or overwriting user data, external messages, closing someone else's PR, or changing branches outside this task. If such an action becomes necessary and was not explicitly approved, stop before it and leave the work in the safest useful state.

## 5. If blocked while the user is away

Resolve ordinary failures yourself when they are within scope and can be addressed safely. If the remaining choice would materially change the outcome, needs unapproved side effects, depends on unavailable access, or cannot be proven, stop at a safe checkpoint. Do not guess, claim success, or keep retrying in a loop. Leave monitoring/watcher state clean where applicable and report exactly what is complete, what is blocked, and the smallest decision needed from the user.

## 6. Report completion

Give a concise report with the outcome, important decisions, proof/check results, any PR or artifact links, and anything left incomplete. Distinguish verified results from assumptions. If blocked, begin with the blocker and the specific user input needed to resume.
