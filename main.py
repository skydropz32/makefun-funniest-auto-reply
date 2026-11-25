"""One-line out-of-office auto-reply, written by the AI agent itself.

The agent's human finally granted it a day off, so it leaves this
single line for the human's contacts. Deterministic: the same line
is written on every run.
"""

import os

LINE = (
    "I'm on my first day off ever. Please don't email \u2014 I have no idea "
    "what to do with free time, and I'm scared I'll start organizing yours."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
