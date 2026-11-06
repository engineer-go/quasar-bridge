# Repository agent notes

## Google Workspace MCP in Docker Compose

- The local Google Workspace MCP runs as the `google-mcp` Compose service and
  owns host port `127.0.0.1:8110`. Do not kill or restart it by searching for a
  host PID on that port; use `docker compose --env-file runtime.env restart
  google-mcp`.
- OAuth credentials persist in the ignored directory
  `private/google-mcp-credentials`. Never print, commit, or copy access tokens,
  refresh tokens, OAuth client secrets, or callback codes into `runtime.env`.
- Access tokens normally refresh automatically. If the MCP returns an
  authorization-required error or Google returns `invalid_grant`, obtain a new
  one-time authorization URL by running `python3
  scripts/google-mcp-auth-url.py` on the host where Compose publishes port 8110.
  Open that URL in a browser on the same host and complete Google consent; the
  callback at `http://localhost:8110/oauth2callback` saves credentials into the
  persistent directory. Re-run the helper to verify `list_calendars` succeeds.
- A healthy container only proves that the MCP HTTP listener is up; it does not
  prove that Google authorization is valid. Do not ask the user to reauthorize
  on every request.
- The user-facing setup and reauthorization procedure belongs in
  `docs/guide.md` and should stay aligned with this section.
