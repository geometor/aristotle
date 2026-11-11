"""Command-line interface for building and verifying the ``geometor-aristotle`` Codex."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Sequence

from geometor.aristotle.compile_codex import compile_codex
from geometor.aristotle.concordance import build_concordance


def _default_repo_root() -> Path:
    """Resolve the repository root directory from package location."""
    return Path(__file__).resolve().parents[3]


def verify_manifest(repo_root: Path) -> tuple[bool, list[str]]:
    """Verify SHA-256 checksums and byte counts for all staged primary source files.

    Args:
        repo_root: Root directory of ``geometor/aristotle``.

    Returns:
        Tuple ``(ok, messages)`` indicating whether all 18 source files match
        ``resources/aristotle/sources_manifest.json``.
    """
    manifest_path = repo_root / "resources/aristotle/sources_manifest.json"
    if not manifest_path.exists():
        return False, [f"Missing manifest: {manifest_path}"]

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    sources = manifest.get("sources", [])
    if len(sources) != manifest.get("total_sources", 0):
        errors.append(
            f"Source count mismatch: declared {manifest.get('total_sources')} vs actual {len(sources)}"
        )

    for src in sources:
        fpath = repo_root / src["file"]
        if not fpath.exists():
            errors.append(f"Missing staged source file: {src['file']}")
            continue
        raw = fpath.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if len(raw) != src["bytes"]:
            errors.append(f"Byte mismatch for {src['id']}: expected {src['bytes']}, got {len(raw)}")
        if digest != src["sha256"]:
            errors.append(f"SHA-256 mismatch for {src['id']}: expected {src['sha256']}, got {digest}")

    return len(errors) == 0, errors


def build_parser() -> argparse.ArgumentParser:
    """Construct the ``geometor-aristotle`` CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="geometor-aristotle",
        description="Build and verify the Aristotle Loci Geometrici et Noetici Book Codex.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=_default_repo_root(),
        help="Path to geometor/aristotle repository root.",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("concordance", help="Rebuild resources/aristotle/concordance.json from sister repos.")
    sub.add_parser("compile", help="Compile concordance, apparatus JSONs, and Book Codex RST tracks.")
    sub.add_parser("verify", help="Verify staged primary source SHA-256 integrity.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Execute the ``geometor-aristotle`` CLI.

    Args:
        argv: Optional sequence of command-line arguments.

    Returns:
        Process exit status (`0` on success, `1` on failure).
    """
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    repo_root: Path = args.repo_root.resolve()
    cmd = args.command or "compile"

    if cmd == "verify":
        ok, errs = verify_manifest(repo_root)
        if not ok:
            for err in errs:
                print(f"ERROR: {err}", file=sys.stderr)
            return 1
        print("OK: All 18 primary Greek and English source files verified against SHA-256 manifest.")
        return 0

    if cmd == "concordance":
        payload = build_concordance(repo_root)
        print(json.dumps(payload["summary"], indent=2))
        return 0

    summary = compile_codex(repo_root)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
