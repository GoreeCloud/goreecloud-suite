# GoreeCloud Suite — Repository Specifications

## Repository purpose

`GoreeCloud/goreecloud-suite` owns the dedicated public GoreeCloud Suite website at `suite.goreecloud.com`. It is the first-party directory and explanation surface for GoreeCloud applications, service-layer products, approved umbrella capabilities, and their relationships to GoreeCloud platform systems.

This repository does not replace the canonical application/service specifications under `GoreeCloud/Projects`, individual product repositories, release evidence, or platform-system authority documents.

## Current evidenced baseline

As of the September 1, 2026 `main` revision `002b2ab3ad9febc32eabc14ffce49238c307ebcf`:

- the rendered Suite directory contains 38 application/service cards;
- 5 approved umbrella capability cards are represented;
- 6 substantive GoreeCloud platform systems are represented;
- the current Stable design-system target is Glaze UI 2.1.0;
- approved product artwork is consumed as repository-local, provenance-pinned derivatives of `GoreeCloud/goreecloud-branding-assets`;
- App Store, File Manager, Maps, and Index use their approved canonical identities.

These statements describe the repository source baseline. They do not independently establish runtime implementation, deployment, release authorization, production acceptance, or Stable qualification for the products represented by the directory.

## Platform relationships

Where the Suite website describes the six GoreeCloud platform systems, the relationships are substantive product relationships rather than decorative badges:

- Glaze UI → Design Center
- Privacy Shield → Privacy Center
- Wardveil Security → Security Center
- Everkeep → Continuity Center
- GoreeCloud Mesh → Mesh Center
- GoreeCloud Identity → Identity Center

Public capability and lifecycle claims must remain bounded by implementation evidence from the authoritative product or platform source.

## Design-system contract

The deployable site targets Glaze UI 2.1.0 Stable until a later Glaze revision completes its own required acceptance process and Suite adopts that accepted revision.

The site must preserve the governing Glaze material rule: **Content is solid. Interaction is glazed.** It must preserve the accessibility and adaptive behavior documented by the current Suite Glaze adoption material, including target sizing, keyboard focus, responsive navigation, density behavior, large-text resilience, safe-area handling, reduced motion, reduced transparency, increased contrast, forced colors, deterministic reduced-material/performance fallbacks, and print resilience.

## Product identity contract

Canonical branding authority is `GoreeCloud/goreecloud-branding-assets`.

Suite-local product artwork is a synchronized implementation derivative only. Approved artwork must be validated against its expected Git blob identity. If approved canonical artwork does not exist for a future product, the Suite site must use an explicitly neutral treatment and must not invent or describe a placeholder as an official product identity.

A branding match does not establish product capability, release state, or production readiness.

## Build and deployment contract

Cloudflare Pages production configuration:

- production branch: `main`;
- build command: `python scripts/build_public_site.py`;
- build output directory: `dist`;
- root directory: repository root;
- custom domain: `suite.goreecloud.com`.

The build publishes an explicit allowlist into `dist/`. Repository documentation must not be exposed merely because it exists at repository root.

## Validation and acceptance boundary

Repository validation is performed with `python scripts/validate_site.py` and any additional required CI or browser acceptance checks.

Acceptance is revision-specific. A source change is not production-accepted merely because it builds or passes repository validation. The exact candidate revision must pass applicable preview validation before merge, and the resulting `main` revision must be verified against the deployed `suite.goreecloud.com` artifact. Source, built artifact, and deployed bytes must agree before production acceptance is recorded.

## Licensing status

**Status: Unresolved production-readiness requirement.**

The current repository has no root `LICENSE` file and GitHub does not detect a repository license. No open-source license is therefore asserted by this specification. The governing GoreeCloud open-source requirement means an explicit, approved repository license must be selected and recorded before this repository can satisfy the licensing portion of production readiness.

Until that decision is documented by the appropriate GoreeCloud authority, repository documentation must not imply a license that has not been approved.

## Required repository records

The repository root must retain and keep current:

- `README.md`
- `SPECIFICATIONS.md`
- `FEATURES.md`
- `BENEFITS.md`
- `COMPETITIVE-OBJECTIVES.md`
- `BRANDING.md`

These records complement, but do not supersede, the canonical GoreeCloud project specification and changelog locations.
