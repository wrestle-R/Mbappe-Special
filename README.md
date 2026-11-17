<img src="assets/icon.png" width="120" alt="">

# The Mbappe Special

Made these for how I like working in [T3 Code](https://t3.codes). Ask the important stuff first, write down what we agreed on, then get on with it.

The usual flow is **grilling → to-spec → to-tickets → half-send**. [Eyes of Render](skills/russel/eyes-of-render/SKILL.md) carries the workflow into implementation and checks that the actual UI holds up.

```sh
npx skills add wrestle-R/Mbappe-Special
```

Pick whichever skills you want, or install one directly:

```sh
npx skills add wrestle-R/Mbappe-Special --skill eyes-of-render
npx skills add wrestle-R/Mbappe-Special --skill grilling
npx skills add wrestle-R/Mbappe-Special --skill half-send
npx skills add wrestle-R/Mbappe-Special --skill unslop
```

| Mine | What I use it for |
| --- | --- |
| [half-send](skills/russel/half-send/SKILL.md) | Finish the approved work while I’m away |
| [eyes-of-render](skills/russel/eyes-of-render/SKILL.md) | Workflow, shared theme, compact layouts and rendered checks |
| [russelore](skills/russel/russelore/SKILL.md) | My writing voice |
| [rdp-commit](skills/russel/rdp-commit/SKILL.md) | Short casual commit names |
| [readme-rdp](skills/russel/readme-rdp/SKILL.md) | A little backstory and the useful instructions |
| [tagged-release](skills/russel/tagged-release/SKILL.md) | Sol handles releases, Luna waits, Sol handles the result |

| Upstream copies | What they do |
| --- | --- |
| [mattpocock/grilling](skills/mattpocock/grilling/SKILL.md) | Work through decisions in question rounds |
| [mattpocock/to-spec](skills/mattpocock/to-spec/SKILL.md) | Turn the conversation into a spec |
| [mattpocock/to-tickets](skills/mattpocock/to-tickets/SKILL.md) | Split the plan into complete slices with blockers |
| [mattpocock/setup-matt-pocock-skills](skills/mattpocock/setup-matt-pocock-skills/SKILL.md) | Configure the tracker used by spec and tickets |
| [mattpocock/diagnosing-bugs](skills/mattpocock/diagnosing-bugs/SKILL.md) | Reproduce a bug, test the cause and verify the fix |
| [pstack/unslop](skills/pstack/unslop/SKILL.md) | Remove AI patterns from writing |
| [leonxlnx/design-taste-frontend](skills/leonxlnx/design-taste-frontend/SKILL.md) | Website art direction and design checks |
| [anthropic/frontend-design](skills/anthropic/frontend-design/SKILL.md) | A distinct frontend design direction |

Use the original skill names with `--skill`; the author folders identify where they came from. Copies retain upstream instructions and licenses. The selected pstack helpers are listed in [the skill review](docs/skill-review.md). Exact sources and revisions are in [upstream-sources.json](upstream-sources.json).

Set up the project tracker before `to-spec` and `to-tickets`. Review the ticket breakdown, then give half-send the implementation scope and go-ahead. Earlier answers carry forward. Publishing issues, commits, releases and deployments follows the task’s authorization.

For UI work, choose taste or Anthropic frontend-design as the design lead and use eyes-of-render to check the result. Russelore is for website copy, blogs and text written as me. Unslop is for assistant replies and explanations to me. [The skill review](docs/skill-review.md) explains what fits where.

Taste includes Node 22+ and Chromium tooling; its Claude hooks do not imply automatic T3 support. Tagged-release needs model delegation and completion handoffs. Private working notes stay in ignored `local-docs/`.
