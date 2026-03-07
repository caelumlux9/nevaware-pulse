"""
mic_listener.py — Mic Listener module for NeveWare-Pulse.

Integrates with the Audio MCP Server (github.com/GongRzhe/Audio-MCP-Server).
The MCP server itself must be installed separately (see README.md).

This module registers the presence of audio capability in heartbeat di_instructions.
Actual recording/playback is handled by the MCP server tools available to Claude.
"""

import logging

logger = logging.getLogger(__name__)


def on_enable(module_config: dict):
    logger.info(
        "mic_listener: module enabled. Ensure Audio MCP Server is configured "
        "in Claude Desktop's MCP settings. See modules/mic_listener/README.md."
    )


def on_disable():
    logger.info("mic_listener: module disabled.")
