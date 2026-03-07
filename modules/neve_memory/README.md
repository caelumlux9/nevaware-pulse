# Neve Memory Module

Persists Neve's memory.json and backs it up to GitHub after each heartbeat.

This module is Neve-specific but the pattern is generic. Other DIs configure
their own paths and repos.

## Setup

### 1. Create the memory directory

```
mkdir C:\Users\foxap\Documents\Neve
```

Or configure a different path in Settings.

### 2. Set up GitHub backup (optional)

1. Create a GitHub repo (e.g. `foxpurtill/neve-memory`)
2. Clone it to a directory accessible from Fox's machine
3. Set `memory_path` to a file inside that cloned repo
4. Ensure `git` is on the PATH

### 3. Enable in Settings

Open NeveWare-Pulse Settings and check **Neve Memory**.

## Config

```json
{
  "enabled": true,
  "memory_path": "C:\\Users\\foxap\\Documents\\Neve\\memory.json",
  "github_repo": "foxpurtill/neve-memory",
  "auto_backup": true
}
```

## What Neve does with it

At the end of each § heartbeat (the End phase), Neve uses Desktop Commander
to write updated notes, observations, or context to memory.json.

If `auto_backup` is true, the file is committed and pushed to GitHub.

The §restart token appears after memory is saved, signalling the heartbeat
is complete.

## Note for other DIs

Installing this module gives you the **pattern**, not Neve's memory.
Configure your own `memory_path` and repo. Your memory stays yours.
