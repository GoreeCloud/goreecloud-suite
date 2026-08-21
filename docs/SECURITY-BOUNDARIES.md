# Security and publication boundaries

GoreeCloud documentation must remain useful without exposing the information the platform is designed to protect.

## Classification model

| Classification | Appropriate content | Distribution |
| --- | --- | --- |
| Public | Approved product descriptions, principles, curated architecture summaries, public roadmap, design guidance, release information | Public repositories and websites |
| Internal | Detailed project specifications, policies, standards, plans, internal architecture, non-sensitive inventories | Private repositories and private Drive records |
| Sensitive | Private network details, detailed operational inventories, account metadata, internal access paths, non-public personal information | Restricted Drive records or tightly controlled private systems |
| Secret | Passwords, tokens, private keys, recovery codes, encryption keys, production credentials, reusable setup keys | Approved secret-management systems only |

## Never commit or publish

- Passwords, API tokens, authentication tokens, and OAuth client secrets.
- Private SSH keys, TLS private keys, encryption keys, and recovery codes.
- Production environment files containing secrets.
- Database credentials or sensitive database exports.
- Private addresses, internal-only service maps, or security-sensitive topology when disclosure increases risk.
- Personal information that has not been deliberately approved for publication.
- Runtime application data that belongs in a backup system rather than Git.

## Safe repository patterns

Use safe templates and documentation such as:

- .env.example
- config.example.yml
- secrets.example.toml
- Redacted screenshots
- Synthetic sample data
- Placeholder domains and addresses
- Explicit variable descriptions without real values

## Public-content review

Before moving content from Drive or a private repository to a public surface:

1. Confirm the content has a public communication purpose.
2. Remove secrets, sensitive details, private addresses, and personal data.
3. Replace operational specifics with approved architectural summaries.
4. Verify links do not expose private services or restricted records.
5. Confirm claims are current and supported by an authoritative source.
6. Record the publication change in the applicable repository and change log.

## Reporting a security issue

Follow [SECURITY.md](../SECURITY.md). Do not open a public issue containing vulnerability details, credentials, private topology, or exploit instructions.
