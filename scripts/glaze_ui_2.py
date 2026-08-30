"""Normalize the GoreeCloud Suite public HTML onto Glaze UI 2.0.0 Stable."""

from __future__ import annotations

GLAZE_VERSION = "2.0.0"
GLAZE_PROMOTION_REVISION = "ff3fff4306bd53ea9c0715a7c0d64265bb038617"


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
    )
    for old, new in replacements:
        html = html.replace(old, new)
    return html
