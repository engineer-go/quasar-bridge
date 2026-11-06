#!/usr/bin/env python3
"""Print a fresh Google authorization URL from the local Compose MCP server."""

import json
import re
import shlex
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ENDPOINT = "http://127.0.0.1:8110/mcp"
PROTOCOL_VERSION = "2025-03-26"


def google_account():
    try:
        lines = Path("runtime.env").read_text().splitlines()
    except OSError:
        return ""
    for line in lines:
        if line.strip().startswith("QUASAR_GOOGLE_ACCOUNT="):
            value = line.split("=", 1)[1].strip()
            try:
                fields = shlex.split(value, comments=True)
            except ValueError:
                return ""
            return fields[0] if fields else ""
    return ""


def post(payload, session_id=None):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if session_id:
        headers["Mcp-Session-Id"] = session_id
    request = Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers=headers,
        method="POST",
    )
    with urlopen(request, timeout=25) as response:
        body = response.read().decode(errors="replace")
        messages = []
        for line in body.splitlines():
            if line.startswith("data:"):
                try:
                    messages.append(json.loads(line[5:].strip()))
                except json.JSONDecodeError:
                    pass
        if not messages and body.strip():
            try:
                messages.append(json.loads(body))
            except json.JSONDecodeError:
                pass
        return response.headers.get("Mcp-Session-Id") or session_id, messages


def main():
    account = google_account()
    if not account:
        print("Set QUASAR_GOOGLE_ACCOUNT in runtime.env first.", file=sys.stderr)
        return 1

    try:
        session_id, messages = post(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {},
                    "clientInfo": {"name": "quasar-google-auth-helper", "version": "1.0"},
                },
            }
        )
        if not session_id or not messages or messages[0].get("error"):
            print("Google MCP did not start an MCP session; check docker compose logs google-mcp.", file=sys.stderr)
            return 1

        post(
            {
                "jsonrpc": "2.0",
                "method": "notifications/initialized",
                "params": {},
            },
            session_id,
        )
        _, messages = post(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": "list_calendars",
                    "arguments": {"user_google_email": account},
                },
            },
            session_id,
        )
    except HTTPError as error:
        print(f"Google MCP returned HTTP {error.code}; check docker compose logs google-mcp.", file=sys.stderr)
        return 1
    except (URLError, TimeoutError, OSError) as error:
        print(f"Cannot reach {ENDPOINT}: {error}", file=sys.stderr)
        return 1

    reply = next((message for message in messages if message.get("id") == 2), {})
    result = reply.get("result", {})
    if reply.get("error"):
        print("Google MCP returned an MCP protocol error; check docker compose logs google-mcp.", file=sys.stderr)
        return 1
    if not result.get("isError"):
        print("Google authorization works; list_calendars succeeded. No new token is needed.")
        return 0

    text = "\n".join(
        item.get("text", "")
        for item in result.get("content", [])
        if isinstance(item, dict)
    )
    match = re.search(r"Authorization URL:\s*(https?://\S+)", text, re.IGNORECASE)
    if match:
        print("Open this one-time Google authorization URL in a browser on this computer:")
        print(match.group(1).rstrip(".,;"))
        print("After Google redirects to localhost:8110, run this command again to verify access.")
        return 0

    print("Google MCP could not list calendars and returned no authorization URL.", file=sys.stderr)
    print("Check docker compose logs google-mcp for the error.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
