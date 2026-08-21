# GoreeCloud Suite architecture

GoreeCloud Suite is an application and service ecosystem within the wider GoreeCloud platform. The Suite is not a single monolith: product repositories remain independently buildable and maintainable while sharing platform services, identity, design language, operational practices, and documentation boundaries.

## Layer model

The current platform model is organized into ten cooperating layers:

1. **Infrastructure** — hosts, storage, network, virtualization, and the execution substrate.
2. **Platform foundation** — shared runtime capabilities and core system services.
3. **Identity and access** — authentication, authorization, accounts, roles, and trusted sessions.
4. **Data and storage** — persistent application data, files, databases, indexing, and lifecycle controls.
5. **Integration and automation** — service-to-service interfaces, events, jobs, workflows, and connectors.
6. **Shared user experience** — Glaze UI, navigation conventions, accessibility, and consistent interaction patterns.
7. **Applications and services** — the product portfolio documented in [PORTFOLIO.md](../PORTFOLIO.md).
8. **Operations and observability** — administration, monitoring, logging, maintenance, and support workflows.
9. **Protection and continuity** — privacy, security, backup, recovery, retention, and digital preservation.
10. **Documentation and governance** — specifications, standards, policies, inventories, decisions, and public communication.

These are responsibility boundaries, not a mandate that every deployment use ten separate components.

## Shared platform relationships

```text
People and devices
        |
Shared experience and applications
        |
Identity | data | integration
        |
Operations | protection | continuity
        |
Infrastructure and platform foundation
        |
Documentation and governance spans every layer
```

## Repository boundaries

Each application repository should own:

- Its implementation, build, tests, dependencies, and release process.
- Application-specific configuration and safe examples.
- Deployment, backup, recovery, and operational guidance when applicable.
- Application-specific security considerations.
- Links to shared authorities instead of copied platform policy.

Cross-platform concerns belong in their specific authorities:

- **Glaze UI** owns shared design-system guidance.
- **GoreeCloud Suite** owns the portfolio and shared documentation navigation.
- **Platform and policy Drive records** own approved architecture, standards, plans, and internal inventories.
- **Public websites** publish curated summaries and do not replace internal source records.

## Integration principles

- Prefer explicit, documented interfaces over hidden coupling.
- Keep applications portable and recoverable.
- Centralize identity carefully while preserving least privilege.
- Separate secrets from source code and documentation.
- Make backup and recovery part of system design, not an afterthought.
- Avoid presenting plans, prototypes, repository existence, and production deployments as equivalent states.
- Keep internal topology and sensitive operational details outside public repositories.

## Source of truth

This page is a repository-level summary. The authoritative internal records are linked from [REFERENCE_INDEX.md](REFERENCE_INDEX.md), especially the platform architecture, platform layers, integration, and Native Applications Plan documents.
