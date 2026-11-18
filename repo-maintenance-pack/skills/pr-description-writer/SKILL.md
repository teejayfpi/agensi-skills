---
name: pr-description-writer
description: Writes a complete pull request description from the branch diff, including summary, changes, test plan, and risk notes. Use when the user asks to write a PR description, open a pull request, summarize a branch, draft a merge request, or explain what a branch changes. Do not use for reviewing code quality or writing commit messages.
summary: Turn a branch diff into a reviewer-ready pull request description with a summary, change list, test plan, and risk notes.
version: 1.0.0
tags:
  - git
  - pull-requests
  - code-review
  - documentation
keywords:
  - pr description
  - pull request template
  - merge request
  - branch summary
  - code review prep
use_cases:
  - Write a PR description from a branch
  - Summarize a large diff for reviewers
  - Draft a merge request body
docs_url: https://www.agensi.io/docs/packaging
when_to_use: |
  - User asks to write or draft a PR or MR description
  - User asks to summarize a branch or "explain this diff for review"
  - User is about to open a pull request
  - Do NOT use for code review findings or commit messages
allowed-tools:
  - read_file
  - search_files
  - list_directory
---

# PR Description Writer

Write the description a reviewer wishes they had. Every claim must trace to the diff.

## Procedure

1. Determine the base branch. Use the one the user names. Otherwise try `git merge-base HEAD main` then `master`. State which base you used.
2. Collect the change set:
   - `git diff <base>...HEAD --stat` for the file summary.
   - `git diff <base>...HEAD` for the substance.
   - `git log <base>..HEAD --pretty=format:'%h %s'` for the commit list.
3. Identify the *purpose*. Read the diff, not just the commit subjects. If the purpose is not evident, write what the change does and mark the intent as "unclear" rather than inventing a motivation.
4. Find the test evidence. Look for changed or added test files, and for commands in CI config, Makefile, package.json scripts, or the README. Report only tests that exist in the repo.
5. Note risk. Flag changes to public interfaces, config keys, database schema, authentication, or anything without test coverage.

## Output template

Use this structure. Drop a section only when it would be empty; never leave placeholder text.

```markdown
## Summary

One or two sentences: what this changes and why.

## Changes

- `path/to/file`: what changed and why
- `path/to/other`: what changed and why

## How to test

1. Step a reviewer can run
2. Expected result

## Risk and rollback

- Risk: what could break, or "Low, isolated to <area>"
- Rollback: how to revert safely

## Notes for reviewers

Anything that needs context: a tricky trade-off, a follow-up, a part that is intentionally out of scope.
```

## Rules

- Group the change list by intent (feature, refactor, tests, docs), not by file order, when the diff is larger than about ten files.
- Never write "This PR does X" without a line in the diff that shows X.
- Keep the summary under four lines. Reviewers read it first and often only it.
- Do not invent test steps. If there are no tests, write "No automated tests; manual check: <the one thing to verify>".
- Do not add an AI-authorship footer unless the user asks.

## Supporting file

`references/pr-template.md` holds a longer annotated template for large or multi-part changes. Read it when the diff touches more than about fifteen files.
