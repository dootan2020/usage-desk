# Publisher signing


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
