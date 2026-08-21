# Security policy

## Reporting

Report suspected vulnerabilities privately. Use a private GitHub Security Advisory for the affected repository when that feature is available. If it is not available, use an existing access-controlled GoreeCloud coordination channel.

Do not open a public issue containing:

- Vulnerability details or exploit steps.
- Credentials, tokens, private keys, or recovery codes.
- Private network topology or internal service addresses.
- Sensitive logs, database content, or personal information.

## Scope

This repository primarily contains portfolio and documentation material. Security reports may still apply to:

- Links that unintentionally expose restricted resources.
- Published secrets or sensitive operational details.
- Documentation that recommends an unsafe configuration.
- Cross-repository guidance that weakens authentication, authorization, privacy, backup, or recovery controls.

## Response principles

- Preserve evidence without spreading sensitive details.
- Revoke or rotate exposed credentials immediately through the appropriate secret-management process.
- Correct the authoritative source and every derived public summary.
- Record the remediation in the appropriate private change log.
- Publish a sanitized advisory only when disclosure is safe and useful.

See [docs/SECURITY-BOUNDARIES.md](docs/SECURITY-BOUNDARIES.md) for classification and publication rules.
