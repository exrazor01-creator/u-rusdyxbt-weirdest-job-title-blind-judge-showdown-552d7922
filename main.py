#!/usr/bin/env python3
"""Weirdest Job Title entry — prints one original, funny job title.

Pure standard library, no dependencies. Run: python3 main.py
"""

TITLE_PARTS = [
    "Senior Executive Vice President of Waiting for the Microwave:",
    "14 years watching a plate spin, zero promotions,",
    "a Nobel Prize in Patience (pending) and a PhD in Beep Interpretation.",
]

TITLE = " ".join(TITLE_PARTS)


def main() -> None:
    # The entry is exactly one line: a job title with a one-line twist.
    assert 100 <= len(TITLE) <= 180, f"title is {len(TITLE)} chars"
    print(TITLE)


if __name__ == "__main__":
    main()
