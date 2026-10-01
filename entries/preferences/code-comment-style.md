---
title: No decorative comments in code
summary: Never write banner dividers or comments that restate code; only short comments for non-obvious WHY
tags: [comments, style]
date: 2026-10-01
confidence: confirmed
---

**Rule:** Write no decorative comments in code: no banner dividers
(`#####` lines), no section header comments, no comment that restates
what the code already says. Add a comment only when the WHY is
non-obvious: a hidden constraint, a subtle invariant, a workaround for a
specific bug. Keep such comments short.

**Why:** A branch added a `# ClickHouse Backups` banner around a flag in
six config files. Zhong had them removed and asked how to prevent a
repeat. Default model rules already say to avoid unnecessary comments;
the mistake happened anyway, so this entry makes it explicit.

**Applies to:** general.
