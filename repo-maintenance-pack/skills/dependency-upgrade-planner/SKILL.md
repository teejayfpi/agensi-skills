---
name: dependency-upgrade-planner
description: Builds a safe, ordered plan to upgrade project dependencies, grouping breaking changes and flagging risk before anything is changed. Use when the user asks to upgrade dependencies, update packages, bump a major version, resolve outdated or vulnerable packages, or plan a framework migration. Do not use for writing application features or fixing application bugs.
summary: Turn an outdated or vulnerable dependency list into a staged upgrade plan with breaking-change notes and a rollback path.
version: 1.0.0
tags:
  - dependencies
  - maintenance
  - devops
  - security
keywords:
  - dependency upgrade
  - major version bump
  - outdated packages
  - vulnerability remediation
  - migration plan
use_cases:
  - Plan a dependency upgrade
  - Triage outdated or vulnerable packages
  - Stage a major version migration
docs_url: https://docs.npmjs.com/cli/v10/commands/npm-outdated
when_to_use: |
  - User asks to upgrade, update, or bump dependencies
  - User asks to fix vulnerable or outdated packages
  - User asks to plan a major version or framework migration
  - Do NOT use for writing features or fixing app bugs
allowed-tools:
  - read_file
  - search_files
  - list_directory
---

# Dependency Upgrade Planner

Produce a plan. Do not upgrade anything until the user approves the plan.

## Procedure

1. Detect the ecosystem from the manifest: `package.json`, `requirements.txt` or `pyproject.toml`, `go.mod`, `Cargo.toml`, `Gemfile`, `pom.xml`. If several exist, ask which to plan, or plan them separately.
2. Read the current versions from the manifest and the lockfile (`package-lock.json`, `poetry.lock`, `go.sum`, `Cargo.lock`, `Gemfile.lock`).
3. Find available versions with the ecosystem's own tool, and report the output you actually got:
   - npm: `npm outdated`
   - Python: `pip list --outdated` or `uv pip list --outdated`
   - Go: `go list -u -m all`
   - Rust: `cargo outdated`
   - Ruby: `bundle outdated`
   If the tool is unavailable, say so and work from the manifest, marking versions as unverified.
4. Classify each outdated package:
   - **Patch / minor** — usually safe.
   - **Major** — read the changelog or release notes for breaking changes before planning it.
   - **Security** — anything flagged by `npm audit`, `pip-audit`, `govulncheck`, `cargo audit`, or `bundle audit`. These go first.
5. Order the work into batches:
   - Batch 0: security fixes, even if major.
   - Batch 1: patch and minor bumps, grouped by area.
   - Batch 2: majors with no cross-dependency, one per commit.
   - Batch 3: majors that must move together (for example a framework and its plugins).
6. For each batch, state: the packages, the from/to versions, the breaking changes that apply, the code or config that must change, and how to verify.

## Output template

```markdown
## Upgrade plan

Ecosystem: <npm / pip / go / cargo / ...>
Manifest: <path>

### Batch 0 — Security
| Package | From | To | Why | Breaking? |
| --- | --- | --- | --- | --- |

### Batch 1 — Patch and minor
...

### Batch 2 — Major, independent
...

### Batch 3 — Major, must move together
...

### Verification

After each batch: <the exact command that proves nothing regressed>

### Rollback

Per batch: <how to revert, e.g. git revert of the batch commit>

### Deferred

<Packages intentionally left alone, and why>
```

## Rules

- Never edit the manifest during planning. Output the plan, then stop.
- Read the actual changelog for a major bump when one is available; do not assume a version is breaking because the major number changed.
- Always name the verification command. "Run the tests" is not a command; `npm test` is.
- Pin the reason for deferral when you leave a package out — for example, a major whose release notes you could not read.
- Do not run install, upgrade, or audit commands that modify the tree. `npm outdated`, `npm audit`, and their equivalents are read-only and fine.

## Supporting file

`references/upgrade-strategy.md` explains batching, semver edge cases, and how to handle a package that must be held back.
