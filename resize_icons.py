#!/usr/bin/env python3
"""
image.png をリサイズして PWA 用アイコンを生成するスクリプト。
usage: python resize_icons.py <input_image> <output_dir>
"""
import sys
from pathlib import Path
from PIL import Image

SIZES = [
    (192, "icon-192.png"),
    (512, "icon-512.png"),
    (180, "apple-touch-icon.png"),
    (32,  "favicon-32.png"),
    (16,  "favicon-16.png"),
]


def main():
    if len(sys.argv) < 3:
        print("Usage: resize_icons.py <input_image> <output_dir>")
        sys.exit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)

    img = Image.open(src).convert("RGBA")
    print(f"元画像サイズ: {img.size}")

    for size, filename in SIZES:
        resized = img.resize((size, size), Image.LANCZOS)
        out_path = dst / filename
        resized.save(out_path, "PNG")
        print(f"  生成: {out_path} ({size}x{size})")

    print("完了")


if __name__ == "__main__":
    main()
