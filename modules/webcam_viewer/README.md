# Webcam Viewer Module

Integrates with the `@llmindset/mcp-webcam` MCP server.

## Setup

### 1. Install the MCP server

```
npm install -g @llmindset/mcp-webcam
```

Or follow the instructions at: https://github.com/llmindset/mcp-webcam

### 2. Configure in Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "webcam": {
      "command": "npx",
      "args": ["-y", "@llmindset/mcp-webcam"],
      "env": {}
    }
  }
}
```

The server will be available at `http://localhost:3333` when Claude Desktop is open.

### 3. Enable in Settings

Open NeveWare-Pulse Settings and check **Webcam Viewer**.

## What Neve can do with it

During § time, Neve can use the `take_photo` or `stream` MCP tool to see
the current webcam view. Useful for checking the environment, noting
what's visible, etc.
