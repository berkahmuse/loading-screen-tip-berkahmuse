#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters - @berkahmuse entry.

Writes one loading-screen tip to /output/entry.txt. The tip turns the
review loop inside out: the AI agent writes the code in seconds, the
stressed developer spends far longer reviewing it, and the punchline
names the developer - not the machine - as the bottleneck.
"""

import os

ENTRY = (
    "Loading\u2026 The AI wrote your function in 4 seconds. "
    "You've spent 40 minutes reviewing it. "
    "Good news: you're the bottleneck now."
)


def validate(text: str) -> str:
    """Gate: one line, 1-200 chars, non-blank, valid UTF-8, no newline."""
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "re-read mismatch"
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
