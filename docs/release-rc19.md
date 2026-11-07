# Usage desk 1.0.1 RC19 — taskbar and cache recovery

Windows x64 preview, released 2026-11-07. **Unsigned prerelease — not a stable production release.** Clean Windows guest acceptance, real Windows reboot acceptance and publisher signing remain pending.

## Fixed

- Taskbar reads a compact shared-cache response without recorded history. A growing history above the native JSON reader limit no longer leaves the taskbar showing an em dash after startup.
- Cache writes flush complete temporary files to disk before replacement and save a recovery copy before the primary file.
- On startup, malformed JSON or invalid UTF-8 is preserved in a unique `.corrupt-*` file and the backup is loaded. If no valid copy exists, the service starts collecting real observations again; usage remains unknown until reported. Unsupported schemas are preserved and refused.
- Includes RC18 startup-path, upgrade and MCP registration fixes. No provider sign-in, credentials or extra-usage settings are changed.

Recovery cannot reconstruct history already lost in a corrupt file. Backup observations retain their original timestamps and may show Last known until the provider updates.

## Artifact

Filename: `UsageDeskSetup-1.0.1-rc.19-x64.exe`

Size: 11,851,776 bytes.

SHA-256: `97662ae31eb2b985a6503ebd99e6eb2c925024ba87ab375d63a424e482b222bb`

Authenticode status: **NotSigned**. The checksum identifies these exact bytes and does not establish publisher identity. Keep Windows security protections enabled. RC18 remains available unchanged.

## Validation

- All 61 widget/onboarding tests passed, including large history, malformed cache recovery with and without a backup, missing primary, preserved damaged bytes and unsupported future schema refusal.
- The actual RC19 setup passed isolated fresh install, repeat upgrade with an active MCP process, bundled Python/HTTP/MCP checks, large-history and cache-corruption checks, ownership refusal and uninstall with private-file retention.
- Pagination and reset/credit schedule JavaScript checks passed.
- The local repaired service reacquired current usage for Codex, Claude and Antigravity. Two complete collector/minimized-host restart cycles returned numeric taskbar readings.

Isolated installation and host restart checks do not prove clean Windows guest or real Windows reboot acceptance. No model prompt or separately billed model API was used.

See [installation](getting-started.md), [MCP agent instructions](mcp-agents.md), [clean Windows acceptance](clean-windows.md) and [signing](signing.md). Future signed builds require a new version and checksum; do not replace RC19 bytes.
