# PR description template (annotated)

Use the short template in SKILL.md for most branches. Reach for this version when a
change is large, multi-part, or reviewer-hostile. The annotations say what each
section is for; delete them in your output.

## Summary

One or two sentences. Answer: what changes, and why now. A reviewer should be able
to decide whether to read the rest from this alone.

## Motivation

Only include when the reason is not obvious from the summary. Link the issue if one
exists. Do not restate the summary.

## Changes

Group by intent:

### Features
- Added X in `path` so that Y

### Refactors
- Moved Z out of `path` into `newpath`; behavior unchanged

### Tests
- Added coverage for A in `tests/path`

### Docs
- Updated `README.md` for the new flag

## Design notes

For changes with a non-obvious approach: what alternatives you rejected and why.
This is where a reviewer's real questions get answered before they ask.

## How to test

Numbered, runnable steps. Include expected output. If a step needs data or a
service, say so.

## Migration

Only for changes that affect users or deployers: config keys added or renamed,
schema changes, required env vars, breaking API changes. Give the before/after.

## Risk and rollback

- Blast radius: which systems or users are affected
- Rollback: the exact revert path, including any data migration that must be undone

## Checklist

- [ ] Tests pass locally
- [ ] Docs updated
- [ ] No credentials committed
- [ ] Breaking changes called out above
