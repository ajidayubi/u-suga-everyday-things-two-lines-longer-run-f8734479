#!/usr/bin/env python3
"""Write the two-line explanation to /output/entry.txt.

Line 1 explains rain to a 10-year-old in one vivid sentence built on a
single analogy: the sky squeezing a giant sponge. Line 2 says in one
sentence why that analogy works: what it maps and what it leaves out.
"""
import os

LINE_1 = "Rain is the sky squeezing a giant sponge over our heads."
LINE_2 = ("It maps how clouds soak up water and let it fall in drops when "
          "they are full, but it leaves out that clouds are made of tiny "
          "floating droplets, not cloth, and rain can fall as snow or hail "
          "instead.")

ENTRY = LINE_1 + "\n" + LINE_2


def main():
    # Self-check the gate before writing: exactly two lines, 1-400 chars.
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
