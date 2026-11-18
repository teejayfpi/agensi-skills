# Conventional Commits quick reference

Source: https://www.conventionalcommits.org/en/v1.0.0/

## Structure

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert.

`feat` and `fix` are the two the spec defines; the rest come from the Angular
convention and are widely accepted.

## Breaking changes

Two equivalent markers:

1. `!` after the type/scope: `feat(api)!: drop the v1 endpoint`
2. A `BREAKING CHANGE:` footer with a description.

A breaking change can appear in any type, not only `feat`.

## Scopes

A noun describing the section of the codebase: `api`, `cli`, `auth`, `deps`.
Keep the project's existing scope names if it already uses them; check recent
history with `git log --oneline -20` before inventing new ones.

## Footer tokens

`BREAKING CHANGE`, `Reviewed-by`, `Refs`, `Co-authored-by`. A footer is
`token: value` or `token #value`.
