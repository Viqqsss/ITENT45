## Ground rules

- When asked to make a code change, suggest a commit message. You may actually perform the commit. Use the Conventional Commits prefixes (e.g., `feat:` `fix:` `chore:` `build:` etc.)
- In general, when asked to make a change, scope your work within your turn to fit cleanly within one commit that can be classified with a Conventional Commit. Tell the human clearly how you scoped your work. If you feel you cannot scope your work cleanly, end your turn and ask the human if you should move forward with the larger scope change.
- `doc/study/`, which will hold study docs, `doc/plan/`, which will hold plan docs, and `doc/wiki/` structure
- Have workflow of updating doc/study/ wherein you will detail the specific the specific feasibility and tradeoffs regarding the prompt then return it as a MD
- After approval there should be a doc/plan/ which you detail the discussed strategy from doc/study/ and list down the concrete steps that will be taken. If changes need to be made, follow the iteration from doc/study/ so that the corresponding plan and study can be followed.
- **study => plan => execute plan => rendezvous => sync docs**

## Common Tasks

### General

- "study": study the requested topic and write a reviewable Markdown document to @./doc/study/{current-unix-timestamp}_{topic}.md. Do not write to any file other than the study doc. Fetch the timestamp before writing. Get the unix timestamp reliably first by running `date +%s` with your shell tool. Commit it under a `docs:` conventional commit.
- Multi-file studies use the same naming convention, just instead of a Markdown doc, use a directory.
  - If a study says `NOTE: `, this came from a human annotation.
- "plan": you will be given a goal/objective -- write a plan in @./doc/plan/{current-unix-timestamp}_{topic}.md for implementation. structure it to be the actual editable task board for another agent session. Commit it under a `docs:` conventional commit.
- If you constitute a plan and require human input, add a prominent "OPEN QUESTIONS" section near the top of the plan doc. Each open question should be brief and self-contained and should prompt the human for an answer. Expect to be asked to "reconstitute the plan" or "fold [the answers] into the plan" with the human answers in mind afterwards.
- "execute plan": you will be given an existing plan doc; your job is to execute the plan. keep track of your progress by editing the plan doc as necessary.
- unless otherwise stated, keep going until either the plan is completed or you hit some sort of roadblock.
- in general, when executing a plan doc, make a new branch.
- "rendezvous", in the context of executing a plan, means to finish the plan execution. The codebase should be in a workable state. Merge the plan changes back to main. Update the docs to reflect the new state of the codebase after plan execution.
- "sync docs": ensure that the living docs accurately reflect the state of the codebase. this is usually run after one or more feature branches has been implemented.
- "collect-commit": commit any uncommitted work appropriately. Use one or more commits.
