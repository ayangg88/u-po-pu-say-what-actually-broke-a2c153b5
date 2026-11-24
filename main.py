"""Say What Actually Broke — one line of honest error copy.

The entry is a single line of software error copy, at most 200
characters, that tells the user the brutal truth about what went
wrong and makes them laugh on the way. It names the real failure
(an expired session), says what to do next (log in again), and
reassures the user their work survived. The twist lands on a single
read — "unlike your session" — and a team could ship this line in a
real dialog without embarrassment.
"""

import os

ENTRY = "Your session expired while you were reading this. Log in again \u2014 your work is safe, unlike your session."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
