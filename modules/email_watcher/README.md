# Email Watcher Module

Polls Gmail for new mail and fires Windows toast notifications.
Also exposes inbox contents during § heartbeat time.

## Setup

### 1. Google Cloud credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (or use an existing one)
3. Enable the **Gmail API**
4. Create OAuth 2.0 credentials (Desktop app type)
5. Download `credentials.json` and place it at:
   `modules/email_watcher/credentials.json`

### 2. First run

On first run, a browser window will open for each watched account.
Authorise access. Tokens are saved to `token_<address>.json` in this directory.

### 3. Enable in Settings

Open NeveWare-Pulse Settings and check **Email Watcher**.

## Config

In `config.json` under `modules.email_watcher`:

```json
{
  "enabled": true,
  "poll_interval_minutes": 5,
  "watched_accounts": [
    {"address": "neve.summersnow@gmail.com", "label": "Neve"},
    {"address": "foxapurtill@gmail.com", "label": "Fox"}
  ],
  "notify_on_new_mail": true,
  "heartbeat_inbox_check": true
}
```

## Dependencies

```
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
plyer  (or win10toast)
```

All installed by `install.py`.

## What Neve can do with it

During § time, Neve can read the inbox summary exposed by this module.
She can note interesting or important messages in her heartbeat response.
She does **not** send emails autonomously — reading and noting only.
