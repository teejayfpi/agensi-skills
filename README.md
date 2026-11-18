# Agensi Skills

Upload-ready `SKILL.md` packages for the [Agensi](https://www.agensi.io) marketplace, plus the copy and steps to publish them.

Three listings, one free funnel and one paid pack:

| ZIP | Listing | Price |
| --- | --- | --- |
| `commit-and-changelog.zip` | Commit & Changelog | Free |
| `dev-environment-doctor.zip` | Dev Environment Doctor | Free |
| `repo-maintenance-pack.zip` | Repo Maintenance Pack | $19 one-time |

Every listing field (name, summary, category, tags, description) is written out in [`SUBMIT.md`](SUBMIT.md).

---

## How to upload to Agensi

There are two ways. Method A is fastest. Method B lets your own agent publish.

### Method A — upload on the website

1. **Sign in.** Go to <https://www.agensi.io> and sign in (Google or email).
2. **Connect payouts** (only needed for the paid pack). Creator dashboard → connect Stripe. Free listings skip this.
3. **Open the submit form:** <https://www.agensi.io/dashboard/submit>.
4. **Upload a ZIP** — start with `commit-and-changelog.zip`. The form reads `summary`, `version`, `tags`, `keywords`, `use_cases` and `docs_url` from the frontmatter and pre-fills the listing.
5. **Paste the remaining fields** from [`SUBMIT.md`](SUBMIT.md): name, summary, category, description, tags, use cases.
6. **Add a logo** (optional): square, 512x512, up to 5 MB.
7. **Submit.** Repeat steps 4-6 for `dev-environment-doctor.zip` (free) and `repo-maintenance-pack.zip` ($19 one-time).
8. **Wait for review.** Most listings are approved within a few hours, up to 48 hours.

### Method B — publish from your own agent (MCP)

Agensi runs a remote MCP server. Your agent needs OAuth, and there is no API key. One agent per account: connecting a new client disconnects others.

1. In your agent (Claude Code, Cursor, OpenClaw, Codex CLI, ...) add the MCP server:
   `https://mcp.agensi.io/mcp/auth`
2. Complete the OAuth sign-in when prompted, in your own browser.
3. Turn on **Creator Mode** in your Agensi dashboard.
4. Point your agent at this folder and ask:
   > Read SUBMIT.md. Publish three skills to Agensi: `commit-and-changelog.zip` and `dev-environment-doctor.zip` as free listings, and `repo-maintenance-pack.zip` as a $19 one-time listing. Use the name, summary, category, tags and description for each from SUBMIT.md. Show me each preview before you confirm.

   The agent previews each listing and waits for your OK before submitting.

### Test a skill locally first

Drop a package folder into your agent's skills directory and confirm it triggers:

- Claude Code: `~/.claude/skills/`
- Then try: "commit this", "my build fails on my machine", "write a PR description for this branch".

---

## Repository layout

```
.
├── SUBMIT.md                      listing copy for all three listings
├── build_zips.py                  rebuilds the ZIPs from source
├── commit-and-changelog/          free listing 1
├── dev-environment-doctor/        free listing 2
├── repo-maintenance-pack/         paid listing (3 skills + shared reference)
└── *.zip                          upload artifacts (gitignored, build with build_zips.py)
```

## Rebuilding the ZIPs

Edit a skill, then:

```bash
python3 build_zips.py
```

This regenerates all three ZIPs from the source folders. The ZIPs are gitignored on purpose: the source folders are the truth, the ZIPs are build output.

## Marketplace rules the packages follow

- Frontmatter is valid YAML; each `name` matches its parent folder exactly.
- Descriptions are trigger-based ("Use when ...", "Do not use for ...").
- No patterns that fail the Agensi security scan: no credentials, no dangerous commands, no prompt-injection phrases.
- Text files only (Agents cannot read images or PDFs).
- Within limits: 100 files / 5 MB per upload, summary <= 300 chars, <= 10 tags, <= 10 keywords, <= 8 use cases.
