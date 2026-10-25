# Usage desk 1.0.1 RC17 — accepted desktop snapshot

Windows x64 preview, frozen on 2026-10-25. This is an unsigned release candidate,
not a stable production release. Clean Windows guest acceptance, a persistent
Windows reboot acceptance run and publisher signing remain pending.

## Changes since RC2

- One main usage view with expandable upcoming resets and recorded history.
- Shared provider card layout and measured account/content pagination.
- Four Antigravity quotas fit together at the tested standard panel sizes.
- Detailed native models and verified context information, clearly separated
  from active client/session capacity and account entitlement.
- Native Claude cloud credit, reported Codex credit and reset metadata.
- Codex credit uses the first recorded local balance as 100%; the baseline is
  retained independently of rolling history and across restarts.
- Taskbar carousel, hover pause, shared cache and local MCP access.
- Stable rounded panel, clipping to the primary display and matching thin edges.
- Pinned keeps the panel open on outside clicks; unpinned dismisses. Hide and
  taskbar toggle close either state. Pin choice survives app/startup restarts.
- Hanoi · UTC+07 display default, with saved Bangkok selections migrated.

## Artifact

Filename: `UsageDeskSetup-1.0.1-rc.17-x64.exe`

Size: 11,850,752 bytes.

SHA-256:
`a761671f83ec4af4a424aba152df525430c65d8548d74fd39191ceabf21424dd`

Only the explicit installer, checksum, release notes and clean-Windows test
bundle are distributed. No installed profile, account identifier, private
telemetry or application source is included in the public repository.

## Validation and limits

Focused widget/onboarding tests, schedule/pagination checks and actual isolated
installer fresh/upgrade/uninstall tests passed. Native tests cover pin
persistence and outside retention, Hide/taskbar dismissal, repeated reversal,
monitor clipping and pixel-edge equality across six DPI scales. The owner
confirmed the desktop appearance and behavior on the developer machine.

Isolated installer tests skip real provider sign-in and integration ownership.
An app-process restart with the Windows logon argument is not a Windows reboot.
Sandbox cannot establish persistence across a guest restart. Windows 10/11 x64
is the intended target; other machines/builds still require acceptance testing.
Provider-native metadata can change upstream. Last known values are retained
truthfully; missing fields are not guessed or converted to zero.

Signing changes the setup hash. A signed release must receive a new version,
regenerated checksum and acceptance run; do not replace these published bytes.
