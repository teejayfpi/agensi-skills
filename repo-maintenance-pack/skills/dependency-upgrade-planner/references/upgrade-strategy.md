# Upgrade strategy notes

## Why batch

One giant upgrade diff is unreviewable and unrevertable. Small batches, each with
its own commit and its own verification, mean a failure points at a handful of
packages, and rollback is a single `git revert`.

## Reading semver

`MAJOR.MINOR.PATCH` — but the number alone does not tell you the risk:

- A `1.0.0` major can be a doc cleanup. Read the changelog.
- A `0.x` project may break in a `0.1` bump; semver gives `0.x` no compatibility
  promise.
- Pre-1.0 and pre-release tags (`-beta.1`, `-rc.2`) move under you. Pin them.
- A "minor" bump can still break you if the project's release notes say so.

Default to reading the release notes for any major, and for any `0.x` bump.

## When a package must be held back

Signals to defer a bump:

- Its peer range blocks another package you cannot move yet.
- The new version drops a runtime or Node/Python version you still support.
- It is a transitive dependency you do not control; the direct parent must move first.
- Its release notes are unavailable or describe a migration you cannot complete now.

Record the deferral and the reason in the plan's Deferred section. A plan that
silently skips a package is worse than one that explains why.

## Peer and transitive dependencies

Direct bumps often force transitive ones. Before finalizing a batch:

```bash
npm ls <package>          # who depends on it, and at what range
npm explain <package>     # why it is in the tree
```

In Python, `pip check` and `uv tree` reveal conflicts. Move a shared dependency in
its own batch so a conflict has one obvious home.

## Verification per batch

Pick the cheapest command that would catch a regression:

| Batch type | Minimum verification |
| --- | --- |
| Patch bumps | Full test suite |
| Minor bumps | Test suite plus a smoke run of the app |
| Security fix | The audit command, confirming the advisory clears |
| Major bump | Test suite, smoke run, and manual check of the changed surface |

## Lockfiles

Commit the lockfile with each batch. A batch that changes the manifest but not the
lockfile is not done — the next install will resolve differently.
