# GoreeCloud Suite Branding

Branding authority: `GoreeCloud/goreecloud-branding-assets`.

The Suite repository must resolve GoreeCloud platform, product, and platform-system branding from the unified repository and its `catalog.json`. Product-local or Suite-local artwork is a synchronized consumer derivative only. New logos, icons, artwork, or identity concepts must be created and approved in the unified branding repository first.

## September 1, 2026 product identity synchronization

The Suite website consumes byte-identical local SVG derivatives for the four product identities newly approved in the canonical branding repository:

| Product | Canonical asset | Canonical Git blob | Suite derivative |
| --- | --- | --- | --- |
| GoreeCloud App Store | `products/app-store/app-icon.svg` | `05c66a2a4c8edcc194183bb8ffb10ca90d8eaeef` | `assets/suite/app-store.svg` |
| GoreeCloud File Manager | `products/file-manager/app-icon.svg` | `c723a84eb2ecb29ef8a0cef845eb1d2cff714cd0` | `assets/suite/file-manager.svg` |
| GoreeCloud Maps | `products/maps/app-icon.svg` | `07b6e52e04c95e1ec9f703a9d323cf799481351c` | `assets/suite/maps.svg` |
| GoreeCloud Index | `products/index/app-icon.svg` | `797cfbd9ae490e37b5a90efe02905159158a8e88` | `assets/suite/index.svg` |

Canonical source revision for this synchronization: `715a2d13e92474a96b107cc66b5f0c026d5911f4`.

The Suite validator pins these exact local Git blobs, requires all four product cards to render their approved SVGs, and rejects regression to the earlier File Manager, Maps, or App Store pending letter-mark placeholders.

Local copies remain implementation derivatives only and must never become independent branding authority. A future canonical artwork revision requires an explicit provenance update and regenerated/re-synchronized derivative.

Branding does not establish application capability, integration, runtime state, release, deployment, production readiness, or Stable qualification.
