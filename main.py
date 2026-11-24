"""One Letter: Coffee or Tea -- entry program.

Writes exactly one letter, "A" for coffee, to the entry file.
Deterministic, standard library only, no network, no input.
"""

import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        # Exactly one character, no trailing newline: the gate
        # scorer requires entry.txt to be 1 to 1 characters.
        f.write("A")


if __name__ == "__main__":
    main()
