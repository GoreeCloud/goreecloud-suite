# Glaze UI 2.0.0 adoption

GoreeCloud Suite targets **Glaze UI 2.0.0 Stable** from `GoreeCloud/goreecloud-glaze-ui`, anchored to Stable promotion reference `ff3fff4306bd53ea9c0715a7c0d64265bb038617`.

The public Suite build publishes a same-origin 2.0 web layer and normalizes the deployable HTML onto the current Stable contract. The integration applies Soft Glaze navigation, Glaze material cards and overview surfaces, Navigation Capsule behavior, 48px interaction floors, connected press/hover transformation, focus-visible semantics, reduced-motion and reduced-transparency handling, increased-contrast support, forced-colors support, and non-backdrop fallbacks.

The integration adds no cross-domain UI runtime dependency. Glaze UI controls presentation and interaction only; application lifecycle, Privacy Shield, Wardveil Security, Everkeep, Mesh, and GoreeCloud Identity state remains producer-authoritative and evidence-scoped.

Source/build validation and rendered Cloudflare Pages acceptance are separate gates. The migration is not treated as production-rendered evidence until the exact reviewed revision passes its deployment checks.