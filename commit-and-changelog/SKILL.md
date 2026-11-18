---
name: commit-and-changelog
description: Writes Conventional Commits messages from staged changes and generates a grouped changelog since the last release tag. Use when the user asks to commit, write a commit message, stage and commit, generate a changelog, write release notes, or summarize what changed since the last version. Do not use for reviewing code quality, fixing bugs, or reverting commits.
summary: Turn staged git changes into a clean Conventional Commits message, and build a grouped changelog since the last tag.
version: 1.0.0
tags:
  - git
  - commits
  - changelog
  - release-notes
  - automation
keywords:
  - conventional commits
  - commit message
  - changelog generator
  - release notes
  - git automation
use_cases:
  - Write a commit message from staged changes
  - Generate a changelog between two tags
  - Draft release notes for a version
docs_url: https://www.conventionalcommits.org/en/v1.0.0/
when_to_use: |
  - User asks to commit, or to write a commit message
  - User asks for a changelog, release notes, or "what changed since vX"
  - User stages files and asks you to "commit this"
  - Do NOT use for code review, bug fixing, or history rewriting
allowed-tools:
  - read_file
  - search_files
  - list_directory
---

# Commit and Changelog

Two jobs, both driven by the git history the agent can already see. Never invent changes that are not in the diff.

## Job 1: Commit message from staged changes

1. Run `git diff --cached --stat` to see what is staged. If nothing is staged, run `git status --short` and tell the user there is nothing to commit. Do not stage files yourself unless the user asked you to.
2. Run `git diff --cached` to read the actual changes.
3. Choose the commit type from this table. If the diff spans several types, pick the dominant one and mention the rest in the body.

   | Type | Use for |
   | --- | --- |
   | feat | A new feature or capability |
   | fix | A bug fix |
   | docs | Documentation only |
   | style | Formatting, no code meaning change |
   | refactor | Code change that is not a fix or feature |
   | perf | Performance improvement |
   | test | Adding or fixing tests |
   | build | Build system or dependencies |
   | ci | CI configuration |
   | chore | Everything else |
   | revert | Reverting a previous commit |

4. Write the message in this exact shape:

   ```
   type(scope): subject

   body (optional)

   BREAKING CHANGE: description (only when a breaking change exists)
   ```

   Rules for the subject line:
   - Imperative mood ("add", not "added" or "adds").
   - Lowercase, no trailing period.
   - 72 characters or fewer, including the type and scope.
   - Scope is the module, package, or area touched. Omit it when unclear.

5. Add a body only when the "why" is not obvious from the subject. Wrap at 72 characters. Explain intent, not mechanics.
6. Add `BREAKING CHANGE:` only when the diff removes or changes a public interface, a config key, or a default.
7. Output the final message in a fenced code block. Then, unless the user said otherwise, run `git commit -m "<subject>" -m "<body>"`.

## Job 2: Changelog since the last release

1. Find the last tag: `git describe --tags --abbrev=0`. If there is no tag, ask the user for the starting point instead of guessing.
2. Read the commits: `git log <tag>..HEAD --pretty=format:'%h %s'`.
3. Group each commit under one of these headings, in this order. Skip a heading when it has no entries.

   - Breaking Changes
   - Features
   - Fixes
   - Performance
   - Refactors
   - Documentation
   - Tests
   - Chores

4. Map commit types to headings: `feat` to Features, `fix` to Fixes, `perf` to Performance, `refactor` to Refactors, `docs` to Documentation, `test` to Tests, `chore`/`build`/`ci`/`style` to Chores. Any commit with `BREAKING CHANGE:` also goes under Breaking Changes.
5. Rewrite each entry as a short user-facing phrase. Drop the type prefix and the scope parentheses, keep the meaning. Do not copy the raw subject line verbatim when it is cryptic.
6. Output:

   ```
   ## [Unreleased] - YYYY-MM-DD

   ### Features
   - Add CSV export to the reports page

   ### Fixes
   - Stop dropping the last row on import
   ```

   Use today's date from the environment. If the user gives a version number, replace `[Unreleased]` with it.

## Boundaries

- Report only what the diff or the log shows. If you cannot tell why a change was made, write the what and leave the why out.
- Do not rewrite, squash, rebase, or force-push history. This skill writes messages and changelogs, nothing else.
- Do not commit when the user only asked for a message.
- If a commit type is genuinely ambiguous, pick the closest one and note the choice in one line after the output.

## Worked example

Staged diff adds a `--json` flag to a CLI command and updates the README.

```
feat(cli): add --json output flag

Emits machine-readable output for scripting. Documented in the README.
```
