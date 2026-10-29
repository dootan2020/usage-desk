# Usage desk 1.0.1 RC18 — startup and MCP fixes

Windows x64 preview, released 2026-10-30. **Unsigned prerelease — not a stable
production release.** Clean Windows guest acceptance, a real persistent Windows
reboot acceptance run and publisher signing remain pending.

## Fixed

- Native host finds the packaged Python runtime and service beside its own
  executable instead of depending on stale absolute launch paths.
- Installer registers physical paths reachable outside a Windows packaged-app
  redirection context, including the runtime, script and owned shortcuts.
- Upgrade skips unchanged payload files, so a connected stdio MCP client can
  keep the bundled interpreter loaded without blocking the update.
- Setup-launched widget has independent standard streams.
- Current agy MCP registration uses `.gemini/config/mcp_config.json` while
  preserving unrelated servers and settings. Codex and Claude registrations
  share the same read-only local usage cache.

## Artifact

Filename: `UsageDeskSetup-1.0.1-rc.18-x64.exe`

Size: 11,851,264 bytes.

SHA-256:
`36ad1bc72f77e1b57e09bf1e3c23a9418fb241e9a4887135b920f898802ed37a`

Windows Authenticode status is NotSigned. The checksum identifies these exact
bytes; it does not establish publisher identity. Do not disable Windows security
protections to install. RC17 remains available as the previous preview; its
published bytes have not been replaced.

## Validation

- 49 widget and 7 onboarding tests passed, plus native launch-path regression
  checks for relocated packages, missing runtime/script and legacy configuration.
- Actual installer passed isolated fresh install, upgrade with a connected MCP
  process, private Python/assets/HTTP/MCP checks, ownership refusal and removal.
- Owner-machine normal upgrade and setup completion passed. Start-menu reopening
  reused one host. The installed Startup shortcut loaded the minimized taskbar
  widget successfully.
- Real cached snapshot reads through all three client registrations passed.
  Claude CLI reported Connected, Codex enabled, and agy listed the server enabled.
- Landing guide and release links were checked separately; no private telemetry,
  credentials, account identifiers or installed profile is in the public assets.

Startup-shortcut testing does not prove a real Windows reboot. Isolated host
tests are not clean-guest acceptance. Reconnect MCP or start a new client session
after updating. Data can remain Last known until the official provider session
supplies fresh usage. No model prompt or paid API is required for MCP cache reads.

See [installation](getting-started.md), [MCP agent instructions](mcp-agents.md),
[clean Windows acceptance](clean-windows.md) and [signing](signing.md).
Future signed bytes must use a new version and checksum; do not replace RC18.
