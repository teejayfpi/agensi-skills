---
name: dev-environment-doctor
description: Diagnoses a broken or inconsistent local development environment and reports the exact fix, covering runtimes, package managers, PATH, permissions, and dependency conflicts. Use when the user asks why a build fails on their machine, says "works on my machine", asks to check their setup, hits a version mismatch, or gets a command-not-found, permission, or dependency error. Do not use for fixing application code or diagnosing production incidents.
summary: Diagnose a broken local dev environment, find the root cause across runtime, PATH, permissions and dependencies, and report the exact fix.
version: 1.0.0
tags:
  - environment
  - debugging
  - developer-tools
  - setup
keywords:
  - environment diagnostics
  - path issues
  - version mismatch
  - works on my machine
  - dependency conflict
use_cases:
  - Diagnose a failing local build
  - Find a runtime version mismatch
  - Fix PATH or permission errors
docs_url: https://www.agensi.io/docs/packaging
when_to_use: |
  - User reports a build or command that fails only on their machine
  - User asks to check or fix their local development setup
  - User hits command-not-found, permission denied, or a version mismatch
  - Do NOT use for application logic bugs or production incidents
allowed-tools:
  - read_file
  - search_files
  - list_directory
---

# Dev Environment Doctor

Find the root cause before proposing any fix. A wrong fix here costs the user more time than no fix.

## Procedure

Work top to bottom. Stop and report as soon as you find the cause; do not run the whole list when the first check explains it.

1. **Reproduce precisely.** Get the exact command and the exact error text. An error string is evidence; "it doesn't work" is not. Ask for the verbatim output if you do not have it.
2. **Check the runtime versions.** Confirm the version the project expects against the one installed:
   - Read the expected version from `.nvmrc`, `.python-version`, `.tool-versions`, `engines` in `package.json`, `go.mod`, `rust-toolchain.toml`, or the README.
   - Read the installed version: `node --version`, `python3 --version`, `go version`, `rustc --version`, `ruby --version`.
   - A mismatch here explains most "works on my machine" failures.
3. **Check which binary is actually running.** `command -v <tool>` and `which -a <tool>`. Multiple installs (system vs version manager) are a common cause; the wrong one wins on PATH.
4. **Check the package manager matches the lockfile.** A `yarn.lock` installed with `npm install`, or a `poetry.lock` ignored by a plain `pip install`, produces phantom dependency errors. Report which lockfile exists and which tool the user ran.
5. **Check dependency state.** Look for a missing or stale install directory (`node_modules`, `.venv`, `vendor`), and for version conflicts (`npm ls <pkg>`, `pip check`, `go mod verify`). A half-finished install is a frequent culprit.
6. **Check permissions and disk.** `permission denied` on a global install usually means the tool is writing to a root-owned path. Check with `ls -ld <path>`. Also check free space if a build fails late with a vague error.
7. **Check environment variables.** Look for a required variable named in `.env.example` or the README that is unset in the current shell (`printenv <NAME>`). Never print the *values* of variables that look like credentials; report only whether they are set.

## Reporting format

```markdown
## Diagnosis

Cause: <one sentence, the root cause>

## Evidence

- <the command you ran> -> <what it returned>

## Fix

<the exact commands, in order>

## Verify

<the command that proves it is fixed>

## If that does not work

<the next most likely cause and its check>
```

## Rules

- State the cause before the fix. Never lead with a fix.
- Give exact commands with real paths and versions, not placeholders.
- Never run destructive commands (deleting a lockfile, wiping `node_modules`, `sudo` installs, reinstalling a global tool) without naming them first and letting the user decide.
- Do not print environment variable values that look like credentials. Report set/unset only.
- If the evidence is inconclusive, say which check would settle it and ask for its output. Do not guess.

## Supporting file

`references/common-failures.md` maps common error strings to likely causes and checks.
