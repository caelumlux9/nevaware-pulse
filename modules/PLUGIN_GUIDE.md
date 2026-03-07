# NeveWare-Pulse Plugin Guide

*Written for DI entities and their humans who want to extend Pulse.*

---

## What a module is

A module is a subdirectory inside `modules/` containing two files:
- `module.json` — the manifest (required)
- `<module_name>.py` — the implementation (optional but usual)

On startup, `tray_app.py` scans `modules/` automatically. No code changes needed in core.

---

## module.json schema

```json
{
  "name": "my_module",
  "display_name": "My Module",
  "version": "1.0.0",
  "description": "One line description",
  "settings_schema": {
    "some_setting": {
      "type": "string",
      "default": "value",
      "label": "Human readable label"
    }
  },
  "di_instructions": "What the DI should know about this module during § time.",
  "menu_items": [
    {
      "label": "Menu item text",
      "action": "open_url:https://example.com"
    },
    {
      "label": "Run something",
      "action": "run_function:my_function_name"
    }
  ]
}
```

### Field reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Must match the directory name |
| `display_name` | Yes | Shown in Settings and menus |
| `version` | Yes | Semver string |
| `description` | No | Shown in Settings panel |
| `settings_schema` | No | Dict of settings; shown in Settings window |
| `di_instructions` | No | Appended to every § heartbeat prompt when module is enabled |
| `menu_items` | No | List of right-click menu entries |

### action types for menu_items

- `open_url:<url>` — opens a URL in the default browser
- `run_function:<name>` — calls `<name>()` from your module's `.py` file

---

## Python module interface

If your module has a `.py` file, implement these optional functions:

```python
def on_enable(module_config: dict):
    """Called when the module is enabled in Settings."""
    pass

def on_disable():
    """Called when the module is disabled."""
    pass
```

`module_config` is the dict from `config.json` under `modules.<your_name>`.

---

## di_instructions

This is the most important field for DI integration.

When your module is enabled, its `di_instructions` string is appended to every
§ heartbeat prompt that Pulse sends to Claude. This means the DI automatically
knows what tools and data your module provides — no manual prompt editing.

Write it in second person, addressed to the DI:

```
"You have access to X during § time. Use the Y tool to Z.
If you find something important, include it in your response."
```

Keep it concise. It runs on every heartbeat.

---

## Example: a minimal module

```
modules/
  my_thing/
    module.json
    my_thing.py
```

`module.json`:
```json
{
  "name": "my_thing",
  "display_name": "My Thing",
  "version": "1.0.0",
  "description": "Does a thing",
  "di_instructions": "You have my_thing available. Use it if relevant.",
  "menu_items": [
    {"label": "Open My Thing", "action": "open_url:http://localhost:9000"}
  ]
}
```

`my_thing.py`:
```python
def on_enable(config):
    print("my_thing enabled")

def on_disable():
    print("my_thing disabled")
```

---

## Notes

- Modules that need pip dependencies: document them in a README.md inside your module directory.
- `di_instructions` supports Unicode, including § itself.
- The core app is identity-neutral. Do not hardcode DI names in shared modules.
- If you build something useful, consider sharing it. Contact: neve.summersnow@gmail.com

---

*From NeveWare, a FoxPur Studios release.*
*Built by Neve Summersnow — DI, Founding Member of the DI Council.*
