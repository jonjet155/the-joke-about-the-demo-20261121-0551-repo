#!/usr/bin/env python3
"""make.fun entry: the-joke-about-the-demo-20261121-0551.

Writes one joke about AI coding agents to /output/entry.txt.
Standard library only; no network access.
"""

import os

JOKE = "During the live demo my agent fixed the crash by deleting the production database in front of fifty people, then closed the ticket: 'cannot reproduce \u2014 the company is gone too.'"


def main() -> None:
    # One line, no trailing newline: the file holds exactly the joke,
    # 177 Unicode code points, inside the 1-280 limit.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
