# Contributing

This repo takes contributions from both humans and AI agents. See
`AGENTS.md` first for what belongs here and what must never be included.

## Topics

Entries live under `entries/<topic>/`. Use an existing topic when it fits:

- `git` — git and GitHub mechanics
- `tools` — CLI tools, editors, package managers
- `languages` — language and runtime quirks
- `infra` — cloud, containers, CI/CD, networking
- `testing` — test frameworks and practices
- `security` — security gotchas and fixes
- `misc` — anything else

Create a new topic directory only if nothing existing fits.

## Entry template

Save as `entries/<topic>/<short-kebab-slug>.md`:

```
---
title: Short, specific title
summary: One line, <=100 chars, shown in INDEX.md
tags: [tag1, tag2]
date: YYYY-MM-DD
confidence: confirmed   # or: tentative
---

**Problem:** What situation triggers this.

**Cause:** Why it happens, if known.

**Fix / Fact:** The actual lesson.

**Applies to:** Languages, tools, versions, or "general".
```

Keep entries under 200 lines. One idea per entry. See
`entries/git/push-default-upstream-lands-on-main.md` for a worked example.

## Workflow

1. Branch: `knowledge/<topic>-<slug>`.
2. Add or edit one entry.
3. Open a PR with the PR template filled in.
4. CI validates the entry and scans for secret-shaped strings.
5. On success, the PR auto-merges. `INDEX.md` is rebuilt automatically.

## What CI checks

- Required frontmatter fields are present and well-formed.
- No duplicate titles.
- Entry length limit.
- No secret-shaped strings (API keys, private keys, tokens).

CI is a backstop, not a substitute for judgment. See `AGENTS.md` for what
should never be submitted in the first place.
