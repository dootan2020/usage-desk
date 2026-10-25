# Clean Windows acceptance

Run in a disposable Windows 10/11 x64 guest with no system Python, previous Usage
desk installation or provider identities. Do not run the clean-guest harness in
the owner's Windows profile. Installer isolation tests on the developer host do
not replace this acceptance.

## Prepared Sandbox run

Enable Windows Sandbox from **Turn Windows features on or off → Windows Sandbox**, then
restart when prompted. Alternatively, in an Administrator PowerShell:

```powershell
Enable-WindowsOptionalFeature -FeatureName Containers-DisposableClientVM -All -Online
```

This is a Windows feature change requiring administrator access and possibly a
restart. Do not change execution policy, disable SmartScreen or share the owner's
home directory. See [Microsoft's prerequisites and installation steps](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install).

Prepare a run from the repository with the exact artifact's SHA-256:

```powershell
powershell -NoProfile -File .\prepare-sandbox-test.ps1 -Setup PATH_TO_SETUP -ExpectedSha256 EXPECTED_SHA256
```

The command prints a unique `.wsb` and results directory. Open that `.wsb` once
Sandbox is available, or pass `-Launch` to the preparation command. Only a copy
of the installer and guest test script are mapped read-only. Only that run's empty
results directory is mapped writable. Clipboard is disabled. Network is enabled
for Microsoft's WebView2 bootstrapper; no provider account is inherited.

The guest writes `clean-windows-result.json` to the mapped results directory.
`PASS_AUTOMATED_INSTALL_LIFECYCLE` means the exact artifact passed fresh normal
per-user installation, private runtime/assets/HTTP onboarding, startup shortcut
registration, upgrade and installed-uninstaller removal. It does not mean all
production gates passed. The report lists untested items explicitly. A failure
leaves the disposable guest open for inspection.

## Persistent VM acceptance

Sandbox cannot validate a persistent Windows restart. Use an existing clean VM
for the remaining checks. Transfer only the published installer, checksum and
this guide; never copy developer credentials, telemetry or browser profiles.

1. Record the Windows build, exact installer hash and WebView2 presence. Test a
   guest without WebView2 to exercise the download/signature/install branch; do
   not remove Windows components from the owner's host to manufacture this case.
2. Install normally as a standard user. Check all Connections cards and the main view, reset/history disclosures and model details at 100%, 125% and 150% display scaling. Confirm no page scrolling and
   reachable account/quota pages and model details.
3. Install official provider clients using their own instructions. Use Connections
   to set up each bridge and complete human sign-in. Verify real quota resets,
   Claude cloud credit and native model choices, and agy Gemini/Claude/GPT pools.
   No model prompt is required. Do not buy credits or enable extra usage.
4. Restart Windows. Without opening a terminal, confirm one host/collector starts,
   taskbar usage appears and data becomes fresh. An expired official credential
   must remain Last known and direct the user to reconnect.
5. Reconnect, switch the official account, temporarily disconnect the network and
   restore it. Check identity separation, rate-limit cooldown and truthful ages.
6. Repeat taskbar open/outside-close/reopen on both monitors, including rapid
   reversal. Pinned should stay open on outside clicks; unpinned should close. Check inset, rounded edges, fade/hover pause and absence of flashes.
7. Upgrade from the previous trusted artifact, restart again, then remove using
   Installed apps. Confirm owned settings restore and private user data remains.

Record PASS/FAIL/NOT RUN per step with UTC timestamps. Do not publish account
identifiers, credentials, private screenshots or setup logs. Re-run against the
final signed artifact: signing changes the distributed file hash.
