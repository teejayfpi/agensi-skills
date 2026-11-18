# Git investigation playbook

Command reference for tracing history. All read-only.

## Blame

| Command | Use |
| --- | --- |
| `git blame <file>` | Last commit that touched each line |
| `git blame -w <file>` | Ignore whitespace-only changes |
| `git blame -C -C <file>` | Follow lines copied within and across files |
| `git blame -L 40,80 <file>` | Limit to a line range |
| `git blame -M <file>` | Detect moved or copied lines within the same file |
| `git blame --since="6 months ago" <file>` | Ignore older commits, show recent ownership |

Blame names the *last* change to a line, which is often a reformat. When that
happens, follow with `-w` and `-C`, or jump to `git log -L`.

## Line-range history

```bash
git log -p -L 40,80:src/app.py          # every change to those lines, with diffs
git log -L :parse_config:src/app.py     # follow a function by name
```

`-L` accepts either `start,end:file` or `:funcname:file`. The function form
survives line-number drift.

## Searching history by content

| Command | Finds |
| --- | --- |
| `git log -S "needle"` | Commits that changed the count of "needle" (add/remove) |
| `git log -G "regex"` | Commits whose diff matches a regex |
| `git log -S "needle" --all` | Include all branches and tags |
| `git log -p -S "needle" -- file` | With diffs, scoped to a file |
| `git log --pickaxe-regex -S "foo.*bar"` | Treat the -S argument as a regex |

`-S` is the fastest way to find when a behavior or constant appeared.

## Filtering the log

```bash
git log --oneline --since="2025-01-01" --until="2025-06-01"
git log --author="Jane" --oneline
git log --grep="migration" --oneline          # search commit messages
git log --merges --oneline                     # merges only
git log --no-merges --oneline                  # exclude merges
git log --follow --oneline -- old/name.py      # survive a rename
git log --diff-filter=D --oneline              # commits that deleted a file
```

## Bisect

```bash
git bisect start
git bisect bad                 # current commit is broken
git bisect good v1.4.0         # this ref is known good
# test at each step, then:
git bisect good | git bisect bad | git bisect skip
git bisect reset               # always finish with this
```

Automate when you have a script that exits non-zero on failure:

```bash
git bisect start HEAD v1.4.0
git bisect run ./scripts/check.sh
git bisect reset
```

Edge cases:
- Untestable intermediate commits: `git bisect skip`, or give a range with
  `git bisect skip <sha1>..<sha2>`.
- Multiple bad commits: bisect names the first one it finds. Repeat from
  `<bad>^` to find others.
- A shallow clone breaks bisect. Run `git fetch --unshallow` first.

## Find who owns an area

```bash
git shortlog -sne -- src/auth/     # contributors to a path, ranked
git log --format='%an' -- src/auth/ | sort | uniq -c | sort -rn
```

## Find the commit that introduced a string, oldest-first

```bash
git log -S "needle" --reverse --format='%h %ad %an %s' --date=short | head -1
```

`--reverse` puts the introduction commit first.
