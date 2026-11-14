<img src="assets/icon.svg" width="64" height="64" alt="">

# The Mbappe Special

Created in [T3 Code](https://t3.codes).

## Half-send

The [`half-send` skill](half-send/SKILL.md) gathers the decisions and approvals needed for a task before starting, then completes the approved work autonomously while you are away.

### Download and install

On GitHub, open [`half-send/SKILL.md`](half-send/SKILL.md) and choose **Raw** to download the skill file, or choose **Code → Download ZIP** to download the repository. To install it for Codex, place the file at:

```text
$CODEX_HOME/skills/half-send/SKILL.md
```

If `CODEX_HOME` is not set, use `~/.codex/skills/half-send/SKILL.md`. Create the `half-send` folder if needed. Then invoke it by saying **half-send** or `$half-send` and describe the task.

Reusable preferences and past-miss notes belong in `local-docs/`. Those two local files are excluded from Git so they stay on this machine and are not pushed to GitHub.
