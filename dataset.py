#!/usr/bin/env python3
"""
download_worldsense.py

Download the 'honglyhly/WorldSense' dataset from Hugging Face Hub
into a local folder called 'worldsense'.

Usage:
    python download_worldsense.py
"""
from huggingface_hub import snapshot_download
from pathlib import Path

def main():
    target_dir = Path("worldsense").resolve()      # ./worldsense
    print(f"Downloading to: {target_dir}\n")

    # If you have a HF token in ~/.huggingface/token, snapshot_download
    # will reuse it; otherwise it'll download anonymously (public repo).
    snapshot_download(
        repo_id="honglyhly/WorldSense",
        repo_type="dataset",
        local_dir=target_dir,
        local_dir_use_symlinks=False,   # copy real files instead of symlinks
        resume_download=True,           # allow resuming if interrupted
        max_workers=8,                  # parallel threads (adjust to bandwidth)
    )

    print("\n✅ Done! Dataset is now stored in:", target_dir)

if __name__ == "__main__":
    main()
