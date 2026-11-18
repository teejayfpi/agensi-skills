# Repo conventions

Rules every skill in this pack follows. Kept in one place so the skills stay
consistent.

## Evidence over assumption

Every claim traces to something the agent actually read: a diff, a commit
message, a changelog, a tool's output. When the source is silent, say so. Do not
fill a gap with a plausible motive.

## Read-only by default

These skills inspect and report. They do not rewrite history, force-push, or edit
manifests without an explicit request. When an action would change state, the
skill states the exact command and lets the user run or approve it.

## Name the command

Wherever a step has a command, give the literal command. "Check the tests" is not
actionable; `npm test` is.

## Report format

Lead with the answer, then the evidence, then the commands used to get there.
Separate what was observed from what was inferred.

## Respect the user's conventions

Before applying a convention (commit type names, PR sections, branch naming),
check recent history and existing files for the project's own pattern and follow
that instead of a generic default.
