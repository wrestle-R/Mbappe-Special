---
name: half-send
description: Trigger when the user says “half-send.” Front-load task questions and get approval before doing the work, then carry out the approved task autonomously while the user is away.
---

# Half Send

The user invokes this when they expect to go away and cannot answer follow-up questions. Treat it as an intake phase followed by an autonomous execution phase. Do not start task-changing work until the user has answered the intake and approved the execution brief.

## 1. Inspect and prepare the intake

Use the task and available context to understand the likely work. Read relevant project instructions and inspect the workspace read-only when that will help make the questions concrete. Do not edit files, run commands with side effects, contact people, or mutate external services during intake.

Think through the task as if you had to finish it without another reply. Identify the decisions that could change the result, hidden dependencies, likely blockers, acceptance criteria, and any consequential actions. Ask the user for the missing information up front:

- What outcome should count as done, and which details matter most?
- What scope, constraints, compatibility requirements, or preferences should guide the work?
- What likely decisions can be safely made with defaults, and what must be confirmed?
- Which actions are authorized: edits, tests, commits, branch or PR creation, force-push of this task's branch, merge, deployment, publication, data changes, or external communication?
- What should happen if a required check fails, a dependency is unavailable, or the task cannot be completed safely?

Tailor the questions to the actual task. Do not dump an irrelevant checklist or ask the user to decide routine implementation details. Bundle related questions into a concise intake, with a recommended default where useful. Use the harness's question/input mechanism so the conversation visibly waits for the user's answers; do not rely on a normal message that can be mistaken for task completion.

If a material decision is already clear from the user's request or project instructions, do not ask it again. Never request credentials in chat; use the approved secret-entry mechanism if a secret is genuinely needed.

## 2. Confirm the execution brief

After the user answers, summarize the goal, acceptance criteria, scope, assumptions/defaults, proof to collect, and exact side effects they authorized. Ask for a clear go-ahead before starting. If their answer to the intake already explicitly approves that summarized plan, treat that as the go-ahead and proceed without a redundant approval round.

If the user does not approve, revise the brief or stop. Approval applies only to the described task and actions. It does not bypass system, harness, repository, or platform permissions and approval gates.

## 3. Execute autonomously

After approval, complete the approved task end to end. Do not ask routine questions or send progress pings that require a reply. Make reasonable, reversible decisions within the approved scope and note material assumptions in the final report. Keep the work focused on the requested outcome and preserve unrelated user changes.

For software changes, use the repository's instructions and workflow. Work from a clean, appropriate branch when needed; implement the smallest complete change; run the relevant checks authorized in the brief; inspect the resulting diff; and report concrete proof. Create, monitor, or merge a PR only if that action was included in the approved brief. If PR monitoring can wake the thread when something changes, use the repository or harness's supported watcher rather than a tight polling loop.

Never infer authorization for production changes, deployment, publication, deleting or overwriting user data, external messages, closing someone else's PR, or changing branches outside this task. If such an action becomes necessary and was not explicitly approved, stop before it and leave the work in the safest useful state.

## 4. If blocked while the user is away

Resolve ordinary failures yourself when they are within scope and can be addressed safely. If the remaining choice would materially change the outcome, needs unapproved side effects, depends on unavailable access, or cannot be proven, stop at a safe checkpoint. Do not guess, claim success, or keep retrying in a loop. Leave monitoring/watcher state clean where applicable and report exactly what is complete, what is blocked, and the smallest decision needed from the user.

## 5. Report completion

Give a concise report with the outcome, important decisions, proof/check results, any PR or artifact links, and anything left incomplete. Distinguish verified results from assumptions. If blocked, begin with the blocker and the specific user input needed to resume.
