#!/usr/bin/env python3
"""Rebuild the upload ZIPs from the skill source folders."""
import os
import zipfile

PACKAGES = [
    ("commit-and-changelog", "commit-and-changelog.zip"),
    ("dev-environment-doctor", "dev-environment-doctor.zip"),
    ("repo-maintenance-pack", "repo-maintenance-pack.zip"),
]


def build(src, out):
    if not os.path.isdir(src):
        raise SystemExit(f"missing source folder: {src}")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(src):
            for f in sorted(files):
                fp = os.path.join(root, f)
                z.write(fp, fp)
    return os.path.getsize(out)


def main():
    for src, out in PACKAGES:
        size = build(src, out)
        print(f"{out:<32} {size:>7} bytes")


if __name__ == "__main__":
    main()
