# GoreeCloud Suite — Features

This file describes features evidenced by the Suite website repository. It does not claim that every application or service displayed by the directory has implemented every capability associated with its category.

## Public product directory

- Dedicated Suite website at `suite.goreecloud.com`.
- 38 currently rendered GoreeCloud application/service cards in the September 1, 2026 baseline.
- Product grouping and lifecycle-oriented presentation.
- Five approved umbrella capability cards.
- Representation of the six substantive GoreeCloud platform systems and their corresponding center relationships.

## Canonical product identity

- Repository-local copies of approved GoreeCloud product artwork for runtime independence.
- Git-blob identity pinning against canonical branding assets.
- Approved App Store, File Manager, Maps, and Index product identities.
- Validation that rejects regression to superseded pending letter marks.
- Neutral fallback requirement when canonical artwork is not yet approved.

## Glaze UI experience

- Glaze UI 2.1.0 Stable source target.
- Responsive navigation and layout behavior.
- General and Touch Assistance interaction-size floors.
- Keyboard focus behavior.
- Comfortable and compact density support.
- Large-text and safe-area resilience.
- Reduced-motion and reduced-transparency handling.
- Increased-contrast and forced-colors behavior.
- Deterministic reduced-material/performance fallback behavior.
- Print resilience.

## Validation and publishing

- Repository validation via `python scripts/validate_site.py`.
- Explicit public build via `python scripts/build_public_site.py`.
- Allowlisted `dist/` publication model rather than automatic exposure of repository contents.
- Cloudflare Pages production configuration for `main` and `suite.goreecloud.com`.
- Revision-specific source, preview, merge, deployment, and production-verification acceptance boundary.

## Documentation boundary

- Repository-local Glaze adoption and architecture material under `docs/`.
- Root governance records that summarize repository specifications, features, benefits, competitive objectives, and branding.
- Explicit separation between directory presentation and authoritative application/service implementation evidence.
