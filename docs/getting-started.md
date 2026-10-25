# Usage desk: install and connect

Usage desk is packaged as a versioned `UsageDeskSetup-VERSION-x64.exe` for Windows 10/11
x64. Setup includes private Python, collector, assets, native host and WebView2
SDK libraries. No repository checkout or system Python is required. Release
artifacts are under `%LOCALAPPDATA%/UsageDeskReleases/VERSION/`. Public downloads
and release status are in [dootan2020/usage-desk releases](https://github.com/dootan2020/usage-desk/releases).
Unsigned release candidates are for acceptance testing; stable publication remains gated.

## Install

1. Obtain the setup executable and matching SHA256SUMS from the trusted distributor.
2. Run setup and choose **Install / update**. Installation is per-user under
   `%LOCALAPPDATA%/FirstmateUsage/`, with Start menu/startup shortcuts and a Windows
   Installed apps entry. Administrator installation is not required.
3. Missing WebView2 is installed using Microsoft's official bootstrapper after
   verifying its Microsoft Authenticode signature. That branch needs Internet;
   provider sign-in and live usage also need Internet.
4. Connections opens on first run. Existing initialized client configurations
   receive bridge/MCP registrations automatically with private backups. Missing
   settings can be initialized from Connections.

The setup is currently unsigned. SHA-256 identifies a file; it does not establish
publisher identity. Do not disable Windows security protections to install it.
Signing and clean Windows VM acceptance remain stable-release gates. See the
[signing handoff](signing.md) and [clean Windows guide](clean-windows.md).

## Connect providers

Each card checks **Official client**, **Bridge & MCP** and **Fresh usage** separately.
An installed bridge or local account alone is not proof of fresh quota.

1. Choose **Get official client** if the Windows CLI is missing. Connections
   re-reads registered PATH entries; use **Check connections** after installation.
2. Choose **Set up connection** to install/repair the bridge and MCP. Existing
   status-line output and unrelated settings are preserved. Conflicting entries
   owned by another integration are refused rather than overwritten.
3. Choose **Sign in / reconnect**. This ensures the bridge is installed, then opens
   the fixed official command in a visible terminal. Complete browser login
   yourself. Never enter a password, API key or login code in Usage desk/chat/MCP.
4. Return and choose **Check connections**. It requests metadata reads through the
   shared collector, without a model prompt or bypassing source rate-limit cooldowns.
   The view refreshes every five seconds; Connected requires recent quota/credit.
5. Choose **Continue to widget**. Missing providers can be left for later without
   inventing data. Reopen Connections from Overview to repair/reconnect. Reconnect
   agent MCP sessions after registration changes.

| Provider | Official sign-in | Current reader |
| --- | --- | --- |
| Codex | `codex login`, then Sign in with ChatGPT | Native account RPC: subscription quota, reported credits and models. API-key mode is not a ChatGPT subscription login. |
| Claude | `claude auth login`, then claude.ai subscription | Native Claude Code profile and subscription credential, used only in memory. Official client owns token refresh. |
| Antigravity | `agy`, then native Google sign-in if requested | Status-line quota and `agy models`. Finish native workspace initialization without sending a prompt. |

Official references: [Codex CLI](https://learn.chatgpt.com/docs/cli),
[Codex auth](https://learn.chatgpt.com/docs/auth),
[Claude setup](https://code.claude.com/docs/en/setup),
[Claude auth](https://code.claude.com/docs/en/authentication),
[Antigravity download](https://antigravity.google/download),
[Antigravity auth](https://antigravity.google/docs/install?tab=cli).

New agy sign-in and subsequent reads share a private `agy-workspace` under the
usage state directory. The collector waits for the first usable callback before
launching idle quota reads. Developer-build migration retains its former workspace;
new installations do not depend on a developer project.

## Connection results

- **Connected**: a recent quota/credit observation exists. Individual model and
  credit fields retain their own observation ages.
- **Not connected**: check official client, bridge and sign-in. A browser-only
  login is insufficient for these native readers.
- **Last known**: cached values remain. Expired sign-in needs reconnect; a rate
  limit needs its cooldown. Failed reads never become invented zeroes.

Normal polling is 120 seconds for Codex/agy and at least 180 seconds for Claude.
Claude model choices refresh independently about every ten minutes using native
control-protocol initialization without a user message. Details include resolved
versions, descriptions, extended-context selectors and reported capabilities.
Default merges into its resolved model. This is the native picker inventory,
not a verified account billing entitlement. Updating it never renews quota or
credit ages. Missing/expired authentication still requires official reconnect.
Manual checks wake metadata readers but preserve rate limits. MCP is optional for
the widget: agents read the same cache and do not log into providers or create a
collector per request.

## Update, remove and recover

Run the next trusted setup to update. It stops the owned host/collector, keeps
telemetry/custom provider metadata and backs up replaced app files. Installed
`launch.txt` points to the bundled runtime/service. It never auto-downloads future
unsigned releases; retain a prior trusted installer for rollback.

Remove via **Settings → Apps → Installed apps → Usage desk → Uninstall**, or
`%LOCALAPPDATA%/FirstmateUsage/UsageDeskSetup.exe --uninstall`. Removal restores
owned client integrations, removes shortcuts/app files and retains telemetry,
browser profile, backups and unrelated files. Conflicting independently modified
configuration entries refuse restore and require review. A temporary removal
runner can remain in Windows Temp.

App backups: `%LOCALAPPDATA%/UsageDeskBackups/`. Private telemetry/client backups:
`~/.firstmate/usage-widget/`. Do not share these private directories as bug reports.
Setup failures are recorded in `UsageDeskSetup-error.log` under Local AppData; an
older log can remain after a successful retry.

## Account and billing limits

Native adapters follow the current local login. Historical accounts paginate
separately; this does not refresh every cached account simultaneously. Reported
credits are automatic where supported and appear in the main provider cards.
There are no separate Timeline/Billing tabs or manual billing controls. Upcoming
native resets and observed history expand below the main view. Subscription
renewal dates and invoices are not retrieved. Older local subscription records
remain private for API compatibility and are excluded from the widget.
Additional providers require a real registry/bridge adapter; installing an unrelated client alone does not add a connection.
