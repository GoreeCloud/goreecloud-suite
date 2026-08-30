"""Normalize the GoreeCloud Suite public HTML onto Glaze UI 2.0.0 Stable.

The source remains intentionally conservative; this build boundary also reconciles
newer first-party products and platform-system language before the public artifact
is validated. Products without approved canonical artwork use a neutral text mark
rather than inventing an official icon.
"""

from __future__ import annotations

GLAZE_VERSION = "2.0.0"
GLAZE_PROMOTION_REVISION = "ff3fff4306bd53ea9c0715a7c0d64265bb038617"

FILE_MANAGER_CARD = '''<article class="app-card"><span class="app-mark app-mark-pending" aria-hidden="true">FM</span><h4>GoreeCloud File Manager</h4><p>First-party file-management experience for local and connected GoreeCloud storage surfaces.</p><span class="badge growing">Active Development</span></article>'''
MAPS_CARD = '''<article class="app-card"><span class="app-mark app-mark-pending" aria-hidden="true">MP</span><h4>GoreeCloud Maps</h4><p>GoreeCloud mapping experience with privacy, location, navigation, and identity boundaries kept explicit.</p><span class="badge growing">Active Development</span></article>'''
APP_STORE_CARD = '''<article class="app-card"><span class="app-mark app-mark-pending" aria-hidden="true">AS</span><h4>GoreeCloud App Store</h4><p>Official multi-user catalog for discovering GoreeCloud applications and services according to account access and entitlement.</p><span class="badge growing">Active Development</span></article>'''
IDENTITY_SYSTEM = '''<div><strong>GoreeCloud Identity · Identity Center</strong><span>identity, authentication, authorization, accounts, devices, credentials, sessions, and delegated authority</span></div>'''


def _insert_after(html: str, anchor: str, addition: str) -> str:
    if addition in html:
        return html
    if anchor not in html:
        raise ValueError(f"Suite content anchor missing: {anchor[:72]}")
    return html.replace(anchor, anchor + "\n            " + addition, 1)


def apply_glaze_ui_2(html: str) -> str:
    replacements = (
        ('name="goreecloud-glaze-ui" content="1.5.0"', 'name="goreecloud-glaze-ui" content="2.0.0"'),
        ('href="glaze-ui-1.5.0.css" data-glaze-ui="1.5.0"', 'href="glaze-ui-2.0.0.css" data-glaze-ui="2.0.0"'),
        ('class="site-header"', 'class="site-header glaze-material-soft"'),
        ('<nav aria-label="Primary navigation">', '<nav class="glaze-navigation-capsule" aria-label="Primary navigation">'),
        ('class="button primary"', 'class="button primary glaze-button"'),
        ('class="button" href="#capabilities"', 'class="button glaze-button" href="#capabilities"'),
        ('class="hero-panel"', 'class="hero-panel glaze-material"'),
        ('Stable 1.5.0 design, interaction, accessibility, motion, material, and form-factor contract', 'Stable 2.0.0 design, interaction, accessibility, motion, material, and form-factor contract'),
        ('Glaze UI 1.5.0', 'Glaze UI 2.0.0'),
        ('Glaze UI 1.5', 'Glaze UI 2.0'),
        ('the five substantive platform systems', 'the six substantive platform systems'),
        ('<div><strong>34</strong><span>current applications & services</span></div>', '<div><strong>37</strong><span>current applications & services</span></div>'),
        (
            'The Suite website uses the reviewed canonical application identity for each product.',
            'The Suite website uses the reviewed canonical application identity when one is approved. Newer products without approved artwork use a neutral text mark until the branding authority publishes a canonical asset.',
        ),
    )
    for old, new in replacements:
        html = html.replace(old, new)

    html = _insert_after(
        html,
        '<article class="app-card"><img src="assets/suite/drive.svg" alt="" width="56" height="56"><h4>GoreeCloud Drive</h4><p>Private multi-user cloud file storage, sharing, collaboration, and version history.</p><span class="badge growing">Milestone 1 Authorization Foundation</span></article>',
        FILE_MANAGER_CARD,
    )
    html = _insert_after(
        html,
        '<article class="app-card"><img src="assets/suite/location.svg" alt="" width="56" height="56"><h4>GoreeCloud Location</h4><p>Original privacy-first multi-user location and tracking platform with explicit access boundaries.</p><span class="badge growing">Active Development</span></article>',
        MAPS_CARD,
    )
    html = _insert_after(
        html,
        '<article class="app-card"><img src="assets/suite/launcher.svg" alt="" width="56" height="56"><h4>GoreeCloud Launcher</h4><p>Original Android home-screen launcher for privacy-first device navigation and GoreeCloud integration.</p><span class="badge growing">Active Development</span></article>',
        APP_STORE_CARD,
    )
    html = _insert_after(
        html,
        '<div><strong>GoreeCloud Mesh · Mesh Center</strong><span>coordination and governance plane for explicit service relationships, dependencies, and evidence exchange</span></div>',
        IDENTITY_SYSTEM,
    )
    return html
