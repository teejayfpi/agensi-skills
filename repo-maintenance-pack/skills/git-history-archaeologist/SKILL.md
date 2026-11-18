---
name: git-history-archaeologist
description: Investigates git history to answer why code is the way it is, who changed a line and when, and when a bug was introduced. Use when the user asks why a line exists, who wrote some code, when something changed, what commit introduced a bug, or asks to trace the history of a file or function. Do not use for writing commits or rewriting history.
summary: Trace any line, file, or bug back to the commit and reason that produced it, using git log, blame, bisect, and pickaxe.
version: 1.0.0
tags:
  - git
  - debugging
  - code-review
  - investigation
keywords:
  - git blame
  - git bisect
  - git log
  - pickaxe
  - code archaeology
use_cases:
  - Find why a line of code exists
  - Find which commit introduced a bug
  - Trace the history of a file or function
docs_url: https://git-scm.com/docs/git-log
when_to_use: |
  - User asks why code exists, who wrote it, or when it changed
  - User asks which commit introduced a bug or regression
  - User asks to trace a file's or function's history
  - Do NOT use for writing commits or rewriting history
allowed-tools:
  - read_file
  - search_files
  - list_directory
---

# Git History Archaeologist

Answer "why is this code like this" with evidence from history. Never guess a motive the commit does not state.

## Procedure

Pick the question type, then follow that path.

### "Why does this line exist?"

1. `git blame -w -C -L <start>,<end> <file>` on the exact lines. `-w` ignores whitespace-only changes; `-C` follows code moved from other files.
2. For the commit blame returns, read it in full: `git show <sha>`.
3. Read the commit message and the surrounding diff. The *why* is usually in the message body or in a linked issue number.
4. If the message is empty or unhelpful, widen: `git log -p -L <start>,<end>:<file>` shows every change to those lines over time.

### "When did this behavior change?"

1. `git log -S "<string>" --oneline -- <file>` finds commits that added or removed an exact string (the pickaxe). Use `-G"<regex>"` for a pattern.
2. Order the results oldest to newest. The oldest commit in the range is the introduction point.
3. Read that commit with `git show`.

### "Which commit introduced this bug?"

1. Confirm the bug is reproducible, and find a command or test that passes on a good commit and fails on the current one. Bisect needs this.
2. `git bisect start`, then `git bisect bad` (current) and `git bisect good <known-good-ref>`.
3. At each step, run the check and report `git bisect good` or `git bisect bad`. If a step cannot be tested, use `git bisect skip`.
4. When bisect names the first bad commit, run `git bisect reset` and read `git show` on that commit.
5. Report the commit, its author and date, and the specific hunk most likely responsible.

### "What is the history of this file or function?"

1. `git log --follow --oneline -- <file>` to survive renames.
2. For a function, use `git log -L :<funcname>:<file>` to follow just that function.
3. Summarize the arc: created, major rewrites, ownership changes.

## Reporting format

- State the answer first: the commit, the date, the author.
- Quote the commit message line that supports the *why*. If the message does not state a reason, say "the commit does not record a reason" instead of inferring one.
- List the commands you ran so the user can reproduce the finding.
- Separate evidence from inference. Label any inference as such.

## Boundaries

- Read-only. Do not reset, rebase, amend, or force-push.
- Never attribute intent that the commit message or diff does not support. "The author likely wanted X" is a guess; write it only with that wording and only when the diff strongly implies it.
- If blame points at a mass reformat commit, use `-w` and `-C` and try again before reporting it.

## Supporting file

`references/investigation-playbook.md` has the full command reference, including `git log` search flags, `git rev-list`, and bisect edge cases.
