# Owner steps before a stable release

The accepted desktop snapshot is 1.0.1-rc.17. Installer SHA-256:
`a761671f83ec4af4a424aba152df525430c65d8548d74fd39191ceabf21424dd`.
No Windows feature, certificate purchase or signing identity was changed.

## Enable Windows Sandbox

1. Save your open work. Open Task Manager → Performance → CPU and check
   Virtualization. If it is disabled, enable the vendor's virtualization option
   in BIOS/UEFI yourself or ask your administrator; do not change unrelated options.
2. Press Windows, search for **Turn Windows features on or off**, open it and
   tick **Windows Sandbox**. Confirm the Windows administrator prompt yourself.
3. Select OK and restart Windows if requested. If the feature is absent or the
   operation fails, report the Windows edition and the exact error. Do not use
   unofficial Home-edition patches or disable Windows protections.
4. Open Windows Sandbox from Start once to confirm it launches, then close that
   empty test window. Sandbox contents are discarded when closed.
5. Open the prepared `UsageDeskAcceptance.wsb` for this release. It maps only
   copied test inputs read-only and a dedicated results folder writable.
   Networking is enabled for Microsoft's WebView2 installer; clipboard sharing
   is disabled. No owner account profile is shared with the guest.
6. Wait for `clean-windows-result.json` in that run's results directory. Share
   the PASS/FAIL result and any error; do not send credentials or private logs.
   Keep the guest open on failure. The automated install result is not proof of
   successful provider sign-in or persistent restart behavior.

The generated test bundle can also be prepared from the downloaded release:

```powershell
Expand-Archive .\UsageDeskCleanWindows-1.0.1-rc.17.zip .\UsageDeskCleanWindows
powershell -NoProfile -File .\UsageDeskCleanWindows\prepare-sandbox-test.ps1 -Setup .\UsageDeskSetup-1.0.1-rc.17-x64.exe -ExpectedSha256 a761671f83ec4af4a424aba152df525430c65d8548d74fd39191ceabf21424dd
```

Follow [Microsoft's Sandbox installation guide](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install).
A persistent clean VM is still needed for sign-in, Windows reboot, reconnect,
multi-monitor and missing-WebView2 acceptance; see the clean Windows guide.

## Prepare publisher signing

1. Decide the legal publisher identity and country. Use the same verified name
   that should appear in Windows. If an approved code-signing certificate already
   exists, retain its current hardware token/HSM or cloud signing provider.
2. Before paying, ask a publicly trusted CA whether it supports Authenticode
   code signing for that identity in Vietnam, the exact validation documents,
   hardware/cloud key requirements and total cost. Complete identity validation
   and any purchase yourself. Do not create an Azure paid subscription merely
   to test eligibility: Microsoft's current Artifact Signing Public Trust
   geography does not include Vietnam. Private Trust does not replace public trust.
3. Install the CA's official token/client tooling and Microsoft's Windows SDK
   Signing Tools. Keep private keys in the token/HSM; do not send a PFX, password,
   recovery code or login token in chat or put them in the repository.
4. Once the certificate is ready, provide only the public certificate thumbprint,
   SignTool path and CA-documented timestamp endpoint. For certificate-store
   signing, inspect the public certificate using:

```powershell
Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert |
  Select-Object Subject, Thumbprint, NotAfter, HasPrivateKey
```

5. The maintainer signs the native host, builds a new package, signs the final
   installer, verifies the publisher/timestamp and regenerates the checksum.
   Re-run acceptance on those signed bytes before a stable release.

Signing does not guarantee immediate SmartScreen reputation. The current EXE
distribution route needs Authenticode; moving to Store-managed MSIX signing
would be a separate packaging project, not a checkbox for this EXE.

Sources verified 2026-10-25:
[Windows signing options](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options),
[Artifact Signing prerequisites](https://learn.microsoft.com/en-us/azure/artifact-signing/quickstart#prerequisites),
[SignTool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).
