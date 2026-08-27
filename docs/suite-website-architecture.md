# GoreeCloud Suite Website Architecture

Date: 2026-08-27

## Decision

GoreeCloud Suite has a dedicated public website at the intended canonical origin `https://suite.goreecloud.com/`.

The main `goreecloud.com` website is the public GoreeCloud hub. It should not duplicate the exhaustive Suite application directory or umbrella-capability catalog. Instead it links to the dedicated Suite website and presents a concise public-websites showcase.

## Suite website responsibility

The Suite website owns public presentation for:

- the complete current GoreeCloud Suite application and service-layer portfolio;
- product grouping and lifecycle/status labels;
- Umbrella Capabilities, including Quill, Waypoint, Resonance, Courier, and Beacon;
- application-versus-capability boundaries;
- canonical cross-client icon identity policy;
- the relationship between Suite products and Glaze UI, Privacy Shield, Wardveil Security, Everkeep, and GoreeCloud Mesh.

It does not replace application repositories, release evidence, private deployment state, source-control authority, or the platform-wide authority documents of the five GoreeCloud platform systems.

## Identity boundary

Glaze UI, Privacy Shield, Wardveil Security, Everkeep, and GoreeCloud Mesh are platform-wide systems and must not be rendered as ordinary Suite applications.

GoreeCloud Identity is a Suite application/service identity. It must not be promoted into the platform-system hero set merely to balance labels or navigation.

Umbrella capabilities are substantial named feature systems inside parent applications, but they are not duplicate standalone Suite applications.

## Application icons

The public Suite directory must use the same reviewed canonical application identity intended for supported web/PWA, Android, desktop/Linux, future iOS, launcher, installer, update, documentation, and recovery surfaces. Platform-specific derivatives may alter masking, padding, dimensions, rasterization, or adaptive layers while preserving the same underlying icon identity.

The initial site consumes the already-reviewed first-party Suite icon assets from `www.goreecloud.com`. A later asset-localization pass may copy the reviewed bytes into this repository so the Suite site can be fully origin-local without changing product identity.

## Deployment

Cloudflare Pages should use:

- repository: `GoreeCloud/goreecloud-suite`;
- production branch: `main`;
- build command: `python scripts/build_public_site.py`;
- output directory: `dist`;
- custom domain: `suite.goreecloud.com`.

The public artifact is explicitly allowlisted. Repository documentation and development files are not published by default.
