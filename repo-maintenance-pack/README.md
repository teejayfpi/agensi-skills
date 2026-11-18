# Repo Maintenance Pack

Three skills that handle the work around your code: describing a change for
reviewers, tracing history when something is unclear, and planning dependency
upgrades safely.

## Included skills

- **pr-description-writer** — turns a branch diff into a reviewer-ready pull
  request description with a summary, change list, test plan, and risk notes.
- **git-history-archaeologist** — answers "why is this line here" and "which
  commit broke this" with evidence from `git blame`, `git log -S`, and `git
  bisect`.
- **dependency-upgrade-planner** — turns an outdated or vulnerable dependency
  list into a staged upgrade plan with breaking-change notes and a rollback path.

## How to use

Install the pack once. Your agent reads each skill's name and description and
loads the right one when your request matches. Ask "write a PR description for
this branch" and it uses the first skill; ask "when did this function change" and
it uses the second; ask "plan our dependency upgrades" and it uses the third.

## What the agent needs

- Git, and a repository to read. All three skills are read-only against your code.
- For the upgrade planner, the ecosystem's own tool (`npm`, `pip`/`uv`, `go`,
  `cargo`, or `bundle`) so it can list outdated versions.

## Boundaries

- None of the skills modify, rebase, or force-push your history.
- The upgrade planner produces a plan and stops. It does not change your manifest
  until you approve.

## Shared reference

`shared/repo-conventions.md` holds conventions every skill in this pack follows.
