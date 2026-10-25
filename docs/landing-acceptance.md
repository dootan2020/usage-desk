# Landing launch acceptance — 2026-10-25

The owner approved the layout, replacement icon set direction, PR #1 merge and
public publication. The original typographic layout is retained. Original SVG
line icons replace Unicode symbols; the three local provider marks identify
products without implying affiliation. No account screenshots or values appear.

## Verified checks

- Desktop/tablet/mobile at 1440px, 768px and 375px: no horizontal overflow,
  broken images or unnamed buttons; nine feature/privacy icons share 1.65px
  strokes. Three carousel logos remain 28px square in all states.
- Product tabs, keyboard arrow navigation, mobile menu, FAQ and checksum copy
  work. The carousel pauses on hover/focus. Page assets and internal anchors
  pass the static checker, including an intentional missing-asset failure test.
- Metadata contrast was measured at 4.44:1 and darkened; body text samples
  exceed 4.5:1. This is a scoped check, not a full screen-reader/AA certificate.
- Only original product copy, fixed release metadata and a labeled illustration
  are served. No customer/account data or local-service URLs are present.
- Release date is visible. Every future release requires an explicit manifest,
  links and documentation update. CI checks the published prerelease and its
  asset names/size; download metadata failure does not create invented values
  or block the static site from rendering.
- GitHub Actions runs on PR/push. Failed validation produces a failing check
  and a visible error annotation. The failure detector was tested with a real
  missing asset in a disposable fixture. Initial CI runs passed:
  https://github.com/dootan2020/usage-desk/actions/runs/40177387976
  https://github.com/dootan2020/usage-desk/actions/runs/40177388891
- No duplicate HTML IDs, broken fragment targets or copied third-party product
  claims were found. Product names match the actual app. Release and download
  origins are the approved dootan2020/usage-desk distribution repository.
- No runtime dependencies, remote icon fonts or analytics are added. CSP blocks
  runtime network connections and external scripts; images are self-hosted.
  Authored illustration styles are the only reason inline styles are allowed.
- Public-tree and staged secret scans passed. No private code, credentials,
  profiles or telemetry were selected. New-tab links have noopener/noreferrer;
  UI updates use fixed DOM targets and textContent rather than HTML injection.

## Owner-approved first-launch exceptions

The gate supports whole-criterion waivers only. The owner explicitly approved
whole rows 1, 2, 3, 4, 8, 9 and 10 for the first public launch, covering missing
real iOS/Android/screen-reader evidence, field INP, Facebook/Zalo preview tests,
production rollback/live monitoring/traffic/vitals and inapplicable translation
requirements. Measured evidence is retained; unmeasured fields remain null.
The exact question and owner reply are recorded in website-scorecard.json.
This result is not an unqualified 10/10. Rows 5, 6 and 7 are not waived.

The site's publication does not certify a stable Windows app release. RC17
remains unsigned; clean guest, persistent Windows reboot and signing acceptance
are pending. Publishing this landing never enables paid model usage or exposes
the loopback collector.

## Maintenance

Run `python tools/check-landing.py --self-test --online` and
`node --check landing/app.js` before changes. Keep release assets immutable.
Edit release metadata only for an accepted new version. Publish the exact saved
Sites source version and verify anonymous HTTP/assets after deployment. Revert
to a previously accepted saved version if a website regression is found.
