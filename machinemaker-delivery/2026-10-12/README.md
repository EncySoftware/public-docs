# Reviewed MachineMaker source snapshot — 2026-10-12 (EN)

This snapshot preserves the reviewed local DocFX sources in the existing public-docs repository.
It is separate from the portal's docs/ tree, whose moved guide sections were removed upstream.

## Manuals

- Фрезерные станки — EN: 31 articles, project `source/milling/docs/machinemaker/machines/docfx.json`.
- Роботы — EN: 47 articles, project `source/robots/main/docfx.json`.
- Токарно-фрезерные станки — EN: 25 articles, project `source/turnmill/main/docfx.json`.

The two language snapshots together contain six manuals and 208 articles. English TurnMilling
uses the shared DocFX template, retains the original numeric article URLs and excludes Trevisan.
The obsolete KB referrals and restricted Custom Imported Robot Cell video link were removed.
The user confirmed the legacy v16 examples; the KUKA link was retained.

## Build and evidence

Use DocFX 2.78.2 and .NET to build an individual project at the path listed above, writing output
outside source/. The project files and referenced binary resources are retained as verified.
Some Milling source links use the previously published shared resource URLs; the English snapshot
contains the canonical shared-resources/ cache used to localize them in the complete delivery.

verification/ records the complete six-book delivery checks, original source provenance,
article/resource hashes, and the delivery archive checksum. The generated HTML and 1.07 GB
delivery ZIP remain in the local workspace and are not duplicated in Git.

The English snapshot also archives the session notes and scripts at their original relative paths
under workspace/. Those scripts document the original local workspace layout; they are not a new
deployment pipeline. Each source project can be built independently using its own docfx.json.

The previous local checks passed: 208 article/link checks, 416 browser page checks, all six book
searches and shared search, original English article-text/resource comparisons, and ZIP CRC.
The full delivery archive SHA256 is `513241f4f0ab16743274fb5d22238056b040f9a56ef10558ecc654cd6eea7e15`.

This feature branch records the reviewed source and verification files. Publication routes and CI integration are a
separate administrator step. No stable or develop branch is changed by this snapshot commit.

## Local screenshot revision after the snapshot commit

Two Robots EN screenshots in Building a kinematic scheme now read "ENCY axes map compatibility mode", as explicitly requested by the user. The source and verification files include this approved revision. Originals are archived outside this source tree. Focused browser checks at 1440/390 px, OCR and the standalone DocFX build passed. The delivery archive and its SHA256 are updated in verification/.

## Server handoff

The ready-made six-manual HTML/admin ZIP is supplied separately as a GitHub draft release asset, tag `machinemaker-six-manuals-2026-10-12`. It is not stored in Git. The checksum above is the current reviewed delivery. Static-site publication remains an administrator step.
