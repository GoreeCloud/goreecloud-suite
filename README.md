# GoreeCloud Suite

GoreeCloud Suite is the first-party application and service layer of GoreeCloud.

This repository now also owns the dedicated public Suite website intended for **https://suite.goreecloud.com/**. The site is separate from the main GoreeCloud homepage so application, service, lifecycle, capability, and product-identity detail has one focused home instead of being duplicated across `goreecloud.com`.

## Website scope

The Suite website covers:

- all current GoreeCloud Suite applications and service-layer products;
- application groups and lifecycle state;
- Umbrella Capabilities such as Quill, Waypoint, Resonance, Courier, and Beacon;
- cross-client application identity and canonical icon policy;
- platform relationships to Glaze UI, Privacy Shield, Wardveil Security, Everkeep, and GoreeCloud Mesh;
- links back to the main GoreeCloud site and source repositories.

## Cloudflare Pages

Recommended production configuration:

- Repository: `GoreeCloud/goreecloud-suite`
- Production branch: `main`
- Build command: `python scripts/build_public_site.py`
- Build output directory: `dist`
- Root directory: blank
- Custom domain: `suite.goreecloud.com`

The build script publishes an explicit allowlist into `dist/` so repository documentation is not automatically exposed.

## Product identity

Application cards use the same reviewed canonical application identities used by the GoreeCloud website and application repositories. Platform-specific derivatives may change size, mask, padding, rasterization, or adaptive layers while preserving the same underlying icon identity.

## Documentation

Existing Suite conformance documentation remains under `docs/`. The public website is a product directory and explanation surface; it does not replace application repositories, release evidence, or platform-system authority documents.
