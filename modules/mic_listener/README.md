# Mic Listener Module

Integrates with the Audio MCP Server by GongRzhe.

## Setup

### 1. Install the Audio MCP Server

```
pip install audio-mcp-server
```

Or from source: https://github.com/GongRzhe/Audio-MCP-Server

Requirements: `sounddevice`, `soundfile`, `FastMCP`

### 2. Configure in Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "audio": {
      "command": "python",
      "args": ["-m", "audio_mcp_server"],
      "env": {}
    }
  }
}
```

### 3. Enable in Settings

Open NeveWare-Pulse Settings and check **Mic Listener**.

## What Neve can do with it

During § time, Neve can use the audio recording tool to listen through the
microphone. Playback and recording are handled entirely by the MCP server.
