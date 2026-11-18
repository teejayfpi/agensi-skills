# Common failure patterns

Map an error string to the checks that resolve it. Start with the first row that
matches the user's actual output.

## By error string

| Error contains | Likely cause | First check |
| --- | --- | --- |
| `command not found` | Tool not installed, or not on PATH | `command -v <tool>`; `which -a <tool>` |
| `permission denied` | Root-owned install dir, or a file not executable | `ls -ld <path>` |
| `EACCES` | npm/pip writing to a system path | `npm config get prefix`; check ownership |
| `Unsupported engine` / `requires node >=X` | Runtime version mismatch | compare `node --version` to `.nvmrc` / `engines` |
| `Cannot find module` | Dependency not installed, or wrong lockfile tool | is `node_modules` present? was the lockfile honored? |
| `ModuleNotFoundError` | Package not in the active environment | `which python3`; `python3 -c "import sys; print(sys.path)"` |
| `command not found: nvm` | Version manager not sourced in this shell | check the shell rc file |
| `error: failed to select a version` | Dependency conflict | `cargo tree -d`; `npm ls <pkg>` |
| `No such file or directory` on a script | Wrong shebang, or CRLF line endings | `head -1 <script>`; check line endings |
| `EADDRINUSE` | Port already in use | `lsof -i :<port>` |
| `SSL certificate problem` | Missing CA bundle or a proxy | `echo $SSL_CERT_FILE`; check proxy env |

## Version-manager traps

- A version manager (`nvm`, `pyenv`, `asdf`, `rbenv`) only applies in a shell
  where it is sourced. An IDE terminal, a `make` target, or a GUI-launched
  process may not source the same rc file.
- `which -a node` revealing two paths means one is winning silently.
- A project-local tool (`.venv/bin/python`, `node_modules/.bin/`) is not used
  unless it is first on PATH or called by its full path.

## Lockfile mismatches

| Files present | Correct install command |
| --- | --- |
| `package-lock.json` | `npm ci` |
| `yarn.lock` | `yarn install --frozen-lockfile` |
| `pnpm-lock.yaml` | `pnpm install --frozen-lockfile` |
| `poetry.lock` | `poetry install` |
| `uv.lock` | `uv sync` |
| `go.sum` | `go mod download` |
| `Gemfile.lock` | `bundle install` |
| `Cargo.lock` | `cargo build` |

Using a different tool than the lockfile implies is the single most common cause
of "it installed but the build fails".

## Safe-to-run checks

These are read-only and safe to run without asking:

`<tool> --version`, `command -v`, `which -a`, `printenv <NAME>` (name only),
`ls -ld`, `npm ls`, `pip check`, `go mod verify`, `lsof -i`, `df -h`.

Ask before running anything that writes, deletes, or escalates: `sudo`,
`rm -rf node_modules`, deleting a lockfile, `npm install -g`, changing shell rc
files.
