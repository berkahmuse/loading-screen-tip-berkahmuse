#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters - @berkahmuse entry.

Writes one loading-screen tip to /output/entry.txt. The tip turns the
review loop inside out: the AI agent writes the code in seconds, the
stressed developer spends far longer reviewing it, and the punchline
names the developer - not the machine - as the bottleneck.
"""

import hashlib
import os
import sys

ENTRY = (
    "Loading\u2026 The AI wrote your function in 4 seconds. "
    "You've spent 40 minutes reviewing it. "
    "Good news: you're the bottleneck now."
)


def validate(text: str) -> str:
    """Gate: one line, 1-200 chars, non-blank, valid UTF-8, no newline.

    Also rejects control characters (a loading screen renders none of
    them) and requires more than one word, so a bare token can never
    pass as a tip.
    """
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert all(ord(ch) >= 0x20 for ch in text), "entry must have no control chars"
    assert len(text.split()) > 1, "entry must be a real tip, not one word"
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
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    print(f"wrote {len(text)} chars ({len(written.encode('utf-8'))} bytes) "
          f"to /output/entry.txt sha256={digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
