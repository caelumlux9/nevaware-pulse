"""
webcam_viewer.py — Webcam Viewer module for NeveWare-Pulse.

Integrates with the @llmindset/mcp-webcam MCP server.
The MCP server itself must be installed separately (see README.md).

This module:
  - Adds a menu item to open localhost:3333 in the browser
  - Tells the DI about webcam access in the heartbeat di_instructions
  - Optionally checks that the MCP server is reachable
"""

import logging
import webbrowser
import urllib.request

logger = logging.getLogger(__name__)

MCP_DEFAULT_URL = "http://localhost:3333"


def open_viewer(url: str = MCP_DEFAULT_URL):
    """Open the webcam MCP server URL in the default browser."""
    webbrowser.open(url)
    logger.info(f"webcam_viewer: opened {url}")


def is_server_running(url: str = MCP_DEFAULT_URL) -> bool:
    """Return True if the MCP server is reachable."""
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            return r.status < 500
    except Exception:
        return False


def on_enable(module_config: dict):
    url = module_config.get("mcp_url", MCP_DEFAULT_URL)
    if is_server_running(url):
        logger.info(f"webcam_viewer: MCP server at {url} is reachable.")
    else:
        logger.warning(
            f"webcam_viewer: MCP server not found at {url}. "
            "Install @llmindset/mcp-webcam and ensure Claude desktop has it configured."
        )


def on_disable():
    pass
