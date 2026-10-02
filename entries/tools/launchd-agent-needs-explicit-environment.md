---
title: launchd agents run with a minimal environment
summary: Homebrew and user-local bin dirs aren't in PATH by default; set PATH/HOME in the plist
tags: [launchd, macos]
date: 2026-10-02
confidence: confirmed
---

**Problem:** A script that works fine run by hand fails silently (or can't
find a command) when run as a `launchd` user agent (LaunchAgent).

**Cause:** launchd does not source the user's shell profile. Its default
`PATH` is just `/usr/bin:/bin:/usr/sbin:/sbin`. Tools installed via
Homebrew (`/opt/homebrew/bin`) or into a user-local bin dir
(`~/.local/bin`) are not found unless the script hardcodes their full path
or the plist sets `PATH` explicitly.

**Fix / Fact:** Add an `EnvironmentVariables` dict to the `.plist` with an
explicit `PATH` (and `HOME`, if the script relies on it):
```xml
<key>EnvironmentVariables</key>
<dict>
    <key>PATH</key>
    <string>/Users/you/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key>
    <string>/Users/you</string>
</dict>
```
Also point `StandardOutPath`/`StandardErrorPath` at log files so failures
are visible, and load with
`launchctl bootstrap gui/$(id -u) <plist>` + `launchctl enable gui/$(id -u)/<label>`
(the modern replacement for `launchctl load -w` on current macOS).

**Applies to:** macOS LaunchAgents/LaunchDaemons running scripts that
depend on Homebrew or user-local tools.
