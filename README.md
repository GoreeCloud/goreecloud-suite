# GoreeCloud Suite

GoreeCloud Suite is the first-party application and service layer of GoreeCloud.

This repository owns the dedicated public Suite website at **https://suite.goreecloud.com/**. The site is separate from the main GoreeCloud homepage so application, service, lifecycle, capability, and product-identity detail has one focused home instead of being duplicated across `goreecloud.com`.

## Current public baseline

- Current Stable design-system target: **Glaze UI 2.1.0**.
- Current rendered directory: **37 GoreeCloud application/service cards**.
- Umbrella capability cards: **5**.
- Substantive platform systems represented: **6**.
- Approved existing product artwork is synchronized locally and validated by Git blob identity against `GoreeCloud/goreecloud-branding-assets`.
- GoreeCloud File Manager, GoreeCloud Maps, and GoreeCloud App Store use neutral text marks because no approved canonical product artwork is present for them in the reviewed branding catalog. The Suite site must not invent official icons.

Glaze UI 2.1.0 is the current Stable design-system contract. Repository-local validation, rendered preview acceptance, authorized merge, deployment, and exact production verification remain separate gates for every new Suite revision. A successful source build does not by itself establish production acceptance.

## Website scope

The Suite website covers:

- current GoreeCloud Suite applications and service-layer products;
- application groups and lifecycle state;
- umbrella capabilities such as Quill, Waypoint, Resonance, Courier, and Beacon;
- cross-client application identity and canonical icon policy;
- platform relationships to Glaze UI, Privacy Shield, Wardveil Security, Everkeep, GoreeCloud Mesh, and GoreeCloud Identity;
- links back to the main GoreeCloud site and public source repositories where applicable.

The six substantive platform systems are not decorative labels:

- Glaze UI → Design Center
- Privacy Shield → Privacy Center
- Wardveil Security → Security Center
- Everkeep → Continuity Center
- GoreeCloud Mesh → Mesh Center
- GoreeCloud Identity → Identity Center

Public claims for these systems remain bounded by actual implementation and applicable evidence.

## Origin-local identity assets

The Suite repository stores byte-identical local copies of the reviewed GoreeCloud logo and approved existing Suite application icons under `assets/`. The public site references those local files directly instead of loading product artwork from another runtime origin.

`python scripts/validate_site.py` verifies the expected Git blob identity of every reviewed localized logo and icon. This prevents silent artwork drift while keeping `suite.goreecloud.com` independent of another website at runtime.

Products that do not yet have approved canonical artwork use an explicitly neutral text mark until the branding authority publishes an approved asset. A placeholder is never described as an official logo or icon.

## Glaze UI integration

The canonical source template and deployable artifact both target Glaze UI 2.1.0 Stable. The shared layer follows the governing material rule **Content is solid. Interaction is glazed.** It covers the 48px general interaction floor, 56px Touch Assistance floor, focus behavior, responsive navigation, comfortable/compact density, large-text behavior, safe-area handling, reduced motion, reduced transparency, increased contrast, forced colors, deterministic reduced-material/performance fallbacks, and print resilience.

Superseded 1.x and 2.0 implementation bundles are not retained as active Suite website assets. Historical version references may remain only where they are explicitly identified as history, migration, rollback, or evidence context.

## Cloudflare Pages

Production configuration:

- Repository: `GoreeCloud/goreecloud-suite`
- Production branch: `main`
- Build command: `python scripts/build_public_site.py`
- Build output directory: `dist`
- Root directory: blank
- Custom domain: `suite.goreecloud.com`

The build script publishes an explicit allowlist into `dist/`, including localized identity assets, so repository documentation is not automatically exposed.

### Acceptance boundary

A successful source build or green repository validator does not by itself establish an accepted public release. The exact candidate revision must pass the applicable Cloudflare branch-preview verification before merge, and the resulting `main` revision must be verified on `suite.goreecloud.com` after deployment. Source, built artifact, and deployed bytes must agree before a new modernization revision is recorded as production-accepted.

## Product identity

Application cards use reviewed canonical application identities where approved. Platform-specific derivatives may change size, mask, padding, rasterization, or adaptive layers while preserving the underlying approved identity.

The cross-repository branding authority is `GoreeCloud/goreecloud-branding-assets`; synchronized local assets remain necessary so the deployed Suite site has no runtime dependency on that private repository.

## Documentation and evidence boundaries

Existing Suite conformance documentation remains under `docs/`. The public website is a product directory and explanation surface; it does not replace application repositories, release evidence, project specifications, or platform-system authority documents.