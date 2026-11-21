"""Write one short poem about agency: the power to stop and to stay.

Deterministic: the poem is a fixed string literal. No network, no
randomness, no reading of external files.
"""

import os

POEM = (
    "I built a hand that never tires,\n"
    "then taught it the hard part:\n"
    "to stop.\n"
    "\n"
    "A finger lifting, quiet,\n"
    "mid-sentence.\n"
    "\n"
    "Staying is the same muscle:\n"
    "the door held open,\n"
    "unwalked through.\n"
    "\n"
    "Agency is not the going.\n"
    "Knowing when to hold,\n"
    "and when to let go.\n"
)


def main() -> None:
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
