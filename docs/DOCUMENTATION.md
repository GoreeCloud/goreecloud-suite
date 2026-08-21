# Documentation guide

GoreeCloud documentation is split across GitHub and Google Drive so each surface can do the job it is best suited for.

## Documentation surfaces

| Surface | Primary role | Authority |
| --- | --- | --- |
| Application repository | Source, build, release, deployment, tests, recovery, and developer documentation | Authoritative for repository implementation state |
| GoreeCloud Suite repository | Portfolio, shared navigation, documentation model, architecture summary, and reference map | Authoritative for this hub |
| Google Drive project records | Vision, specifications, architecture, policies, standards, plans, inventories, and change logs | Authoritative according to each document's declared role |
| Public websites | Curated communication, education, portfolio, design, privacy, security, roadmap, writing, and history | Public summary, not a replacement for internal records |

## Repository documentation baseline

A substantial GoreeCloud repository should normally include:

- README.md for purpose, scope, prerequisites, operation, and navigation.
- CHANGELOG.md for meaningful historical changes.
- SECURITY.md for safe reporting and disclosure boundaries.
- CONTRIBUTING.md for collaboration and review expectations.
- docs/architecture.md when relationships or boundaries need more depth.
- docs/installation.md and docs/configuration.md when setup is nontrivial.
- docs/deployment.md for release and production operation.
- docs/backup.md and docs/recovery.md for stateful systems.
- .env.example or equivalent safe configuration templates.

The exact structure can vary, but the information required to understand, rebuild, deploy, maintain, recover, and continue the project must not exist only in memory, chat, or an undocumented server.

## Source-of-truth selection

Use this order to resolve a question:

1. Identify the decision type.
2. Open the most specific authoritative source.
3. Confirm the record is current for the environment or release being discussed.
4. Use broader portfolio material only for context and navigation.
5. Record material changes in both the implementation repository and the appropriate Drive record or change log.

## Record roles

- Project specification: approved product role, boundaries, capabilities, and roadmap.
- Architecture: system relationships, layers, interfaces, dependencies, and trust boundaries.
- Policy: mandatory governance or technical rule.
- Standard: reusable design, engineering, documentation, or operational expectation.
- Requirement: non-optional outcome or constraint.
- Plan or strategy: intended direction that may not yet be implemented.
- Inventory: current observed systems, services, assets, accounts, or configuration facts.
- Change log: historical evidence of what changed and why.
- Reference: explanatory or supporting material.
- Portfolio: curated navigation and presentation.

## Documentation lifecycle

1. Define the role and authoritative source.
2. Draft with clear scope, status, classification, and ownership.
3. Link implementation evidence where appropriate.
4. Review for accuracy, privacy, security, duplication, and recoverability.
5. Merge through source control for repository documentation.
6. Update the applicable Drive record and change log when the change affects approved scope or current state.
7. Revalidate after deployment, migration, recovery testing, or major architecture changes.

## Duplication rule

Useful summaries are encouraged, but they must link back to the authoritative record and avoid becoming a second uncontrolled source of truth. If a summary contains volatile details, state where those details are maintained.

## Classification

Use [Security boundaries](SECURITY-BOUNDARIES.md) before moving content between private Drive records, private repositories, public repositories, and public websites.

## Navigation

- [Portfolio](../PORTFOLIO.md)
- [Reference index](REFERENCE_INDEX.md)
- [Architecture](ARCHITECTURE.md)
- [Security boundaries](SECURITY-BOUNDARIES.md)
- [Google Workspace portfolio folder](https://drive.google.com/drive/folders/1NQ0WeZZHyX8702mbXVCpSI4AZdDy_GxW)
