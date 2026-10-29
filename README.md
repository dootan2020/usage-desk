# Usage desk

A little clarity. For every model.

A local Windows taskbar widget for Codex, Claude and Google Antigravity usage,
quota resets and reported credits. Click taskbar usage to open the detail panel.
Agents can read the same local cache through MCP.

Read the [MCP instructions for agents](docs/mcp-agents.md) for connection checks,
tool calls, quota/credit interpretation and a copyable instruction block.

## Download

[Download v1.0.1-rc.18 for Windows x64](https://github.com/dootan2020/usage-desk/releases/download/v1.0.1-rc.18/UsageDeskSetup-1.0.1-rc.18-x64.exe)
· [SHA-256 checksums](https://github.com/dootan2020/usage-desk/releases/download/v1.0.1-rc.18/SHA256SUMS.txt)
· [All releases](https://github.com/dootan2020/usage-desk/releases)

**Release candidate — not a stable production release.** The installer is
currently unsigned. Automated host install/upgrade/removal and local runtime
tests passed. Clean Windows guest execution, persistent Windows restart and
publisher signing are still pending. Do not disable Windows security to install.
SHA-256 identifies the file; it does not verify publisher identity.

Windows 10/11 x64 is the intended target. The verified developer host is Windows
11 x64 build 26200; other builds still require acceptance testing. Internet is
required for provider sign-in/live usage and Microsoft's WebView2 installation
when that runtime is missing. Python is included. No source checkout is needed.

## Install and sign in

1. Download the installer and matching checksum from the release above. Verify
   with `Get-FileHash -Algorithm SHA256 .\UsageDeskSetup-1.0.1-rc.18-x64.exe`.
2. Run setup and choose **Install / update**. It installs for your Windows user
   under `%LOCALAPPDATA%\FirstmateUsage`, adds Start menu/startup shortcuts and an
   Installed apps entry. A missing WebView2 runtime is obtained from Microsoft
   after its publisher signature is checked.
3. Open **Connections**. If a client is missing, choose **Get official client**.
   Install its official Windows CLI, then return and **Check connections**.
4. Choose **Set up connection**, then **Sign in / reconnect**. Existing client
   settings are backed up; bridge and MCP entries are configured automatically.
   Complete the provider's login in its own terminal/browser. Never enter a
   password, API key or login code into this widget, MCP or a GitHub issue.
5. Choose **Check connections**. Client installed, bridge installed and fresh usage
   are checked independently. A successful bridge setup alone is not live usage.
6. Choose **Continue to widget**. Connections can be reopened from the main view.

| Provider | Official login | Data source |
| --- | --- | --- |
| Codex | `codex login` → Sign in with ChatGPT | Native account RPC: reported allowance, credits and model inventory. |
| Claude | `claude auth login` → claude.ai subscription | Native subscription usage, reported cloud credit and native client model choices. |
| Antigravity | `agy` → official Google sign-in | Native status-line quota and idle `agy models` metadata. Complete initial workspace setup without a model prompt. |

Official clients: [Codex](https://learn.chatgpt.com/docs/cli),
[Claude Code](https://code.claude.com/docs/en/setup),
[Antigravity](https://antigravity.google/download).

The widget does not sell model access or replace a provider subscription. It
does not submit model prompts. These adapters depend on current native client
metadata; upstream changes can break collection. Native model options, especially
Claude selectors, do not certify account entitlement or a separate quota per model.
Claude details include resolved versions, descriptions and reported capability
support, including extended-context choices such as Fable's `[1m]` selector.
This is an independent utility, not an official provider product.

## Everyday use

- Taskbar carousel rotates every five seconds and pauses on hover. Select
  **Show all 3 providers** to show the three values together.
- One main view shows shared provider cards. Upcoming resets, recorded history
  and model details expand on demand. Accounts and quota pages remain reachable
  without page scrolling. The default timezone is Hanoi · UTC+07.
- Pinned keeps the panel open on outside clicks; unpinned dismisses it. Hide and
  taskbar usage still close it. The pin choice persists across app/startup restarts.
- **Last known** preserves older real data after a failed read. Open Connections
  to reconnect expired official login. Rate limits keep their cooldown. Updates
  to a model catalog never refresh the age of older quota or credit.
- Subscription renewal dates and invoices are not retrieved. Reported credit
  retains its provider units; Codex credit remaining uses the first recorded
  balance as a persistent local 100% reference, not a provider-reported total.
- Agents use the automatically registered `firstmate-usage` MCP server. Reconnect
  the agent's MCP session after setup. Reads use the shared cache and do not
  start another collector or provider login.

## Update, uninstall and privacy

Run the next trusted installer to update. No automatic unsigned update download
is enabled. Remove through **Windows Settings → Apps → Installed apps → Usage
desk**. Owned integrations are restored; private telemetry, browser profile,
backups and unrelated files remain. Independently modified settings are preserved
or require review rather than being overwritten.

Provider credentials stay in their official local clients. The collector reads
native account information locally; it does not upload telemetry to this project
or GitHub. Its HTTP service binds to loopback at `127.0.0.1:17864`; other local
processes may access telemetry. It is not a remotely authenticated cloud service.
Do not expose it through a public tunnel.

Do not attach `~/.firstmate/usage-widget`, client configuration, browser profiles,
tokens, personal usage screenshots or raw logs to public issues. Report the
release version, Windows build and a redacted description instead.

This repository distributes only setup artifacts, checksums and public
instructions. The development repository and owner data remain private.

## Guides and landing page

- [Install and connect](docs/getting-started.md)
- [RC18 changes and validation](docs/release-rc18.md)
- [Clean Windows acceptance](docs/clean-windows.md)
- [Owner Sandbox and signing steps](docs/owner-release-steps.md)
- [Publisher signing](docs/signing.md)
- [Landing page source](landing/) — the public website link is listed in this repository's About section.
- [Website launch checks and first-launch exceptions](docs/landing-acceptance.md)
