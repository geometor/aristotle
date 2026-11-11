"""Sphinx configuration for GEOMETOR • aristotle (Loci Geometrici et Noetici)."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.aristotle as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "aristotle"
repo_name = "aristotle"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

project = "GEOMETOR • aristotle"
author = "Aristotle of Stagira • Ed. GEOMETOR"
copyright = "2026, GEOMETOR • Bekker (1831) & Oxford Translation Critical Codex"

if "geometor.aristotle.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.aristotle.sphinx_ext")  # noqa: F405

# Register local sister inventories when built docs exist; prune unreachable remote-only
# entries so offline builds remain warning-free.
for _sister in ("euclid", "hoenen", "pacioli", "elements", "pappus"):
    _inv = _WORKSPACE_ROOT / _sister / "docs" / "objects.inv"
    if _inv.is_file():
        intersphinx_mapping[_sister] = (  # noqa: F405
            f"https://geometor.github.io/{_sister}",
            (str(_inv), None),
        )

intersphinx_mapping = {  # noqa: F405
    _k: _v
    for _k, _v in intersphinx_mapping.items()  # noqa: F405
    if _v[1] is not None
}

html_theme = "foundation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
autoapi_add_toctree_entry = False
autoapi_options = [opt for opt in autoapi_options if opt != "imported-members"]  # noqa: F405
napoleon_use_ivar = True
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]
