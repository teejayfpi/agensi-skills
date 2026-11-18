# Agensi submission kit

Copy-paste source for the three listings. Field limits: summary <= 300 chars,
<= 10 tags, <= 10 keywords, <= 8 use cases, 100 files / 5 MB per upload.

Submit at https://www.agensi.io/dashboard/submit (sign-in required).

---

## Listing 1 — Commit & Changelog (free)

Upload: `commit-and-changelog.zip`

- **Name:** Commit & Changelog
- **Summary:** Turn staged git changes into a clean Conventional Commits message, and build a grouped changelog since your last release tag.
- **Pricing:** Free
- **Category 1:** Code Quality & Review
- **Tags:** git, commits, changelog, release-notes, automation
- **Use cases:** Write a commit message from staged changes; Generate a changelog between two tags; Draft release notes for a version
- **Compatibility note:** Requires git. Read-only: writes commit messages and changelogs, never rewrites history.
- **Description:** see "Long description" below.

---

## Listing 2 — Dev Environment Doctor (free)

Upload: `dev-environment-doctor.zip`

- **Name:** Dev Environment Doctor
- **Summary:** Diagnose a broken local dev environment — runtime versions, PATH, permissions, lockfile mismatches — and get the root cause plus the exact fix.
- **Pricing:** Free
- **Category 1:** DevOps & Cloud
- **Tags:** environment, debugging, developer-tools, setup
- **Use cases:** Diagnose a failing local build; Find a runtime version mismatch; Fix PATH or permission errors
- **Compatibility note:** Works in any shell. Read-only checks only; asks before any command that changes state.
- **Description:** see "Long description" below.

---

## Listing 3 — Repo Maintenance Pack ($19 one-time)

Upload: `repo-maintenance-pack.zip`

- **Name:** Repo Maintenance Pack
- **Summary:** Three skills that handle the work around your code: reviewer-ready PR descriptions, git history investigation, and safe dependency upgrade plans.
- **Pricing:** One-time, $19
- **Category 1:** Code Quality & Review
- **Tags:** git, pull-requests, dependencies, debugging, maintenance
- **Use cases:** Write a PR description from a branch; Trace why a line exists or which commit broke it; Plan a dependency upgrade with a rollback path
- **Compatibility note:** Requires git. The upgrade planner also uses your ecosystem's tool (npm, pip/uv, go, cargo, bundle). All skills are read-only against your code.
- **Description:** see "Long description" below.

---

## Long descriptions (paste into the Description field)

### Commit & Changelog

Reads your staged diff and writes a Conventional Commits message that follows the
spec: correct type, imperative subject under 72 characters, body only when the
"why" is not obvious, and a BREAKING CHANGE footer only when one exists. It also
builds a changelog since your last release tag, grouping commits into Breaking
Changes, Features, Fixes, Performance, Refactors, Documentation, Tests, and
Chores.

Where it stops: it reports only what the diff and the log show. It does not
review code quality, fix bugs, or rewrite history.

### Dev Environment Doctor

Root-causes the failures that only happen on one machine. It checks runtime
versions against what the project expects, finds which binary is actually running
when several are installed, spots lockfile and package-manager mismatches,
detects stale or missing installs, and flags permission and PATH problems. It
leads with the diagnosis and the evidence, then gives the exact commands to fix
and verify.

Where it stops: it is read-only by default. It names any command that changes
state and lets you decide before it runs.

### Repo Maintenance Pack

Three skills that cover the work around your code:

1. pr-description-writer — turns a branch diff into a reviewer-ready pull request
   description with a summary, grouped change list, test plan, and risk notes.
2. git-history-archaeologist — answers "why is this line here" and "which commit
   broke this" using git blame, log -S, and bisect, with evidence separated from
   inference.
3. dependency-upgrade-planner — turns an outdated or vulnerable dependency list
   into a staged upgrade plan with breaking-change notes and a rollback path.

Where it stops: none of the skills modify, rebase, or force-push your history,
and the upgrade planner produces a plan and stops until you approve.
