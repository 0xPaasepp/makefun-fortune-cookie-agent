# Fortune Cookie for an AI Agent: one original fortune-cookie line for
# an AI agent, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: an agent's whole career arc in one fortune -- honored
# retirement, then an unceremonious reboot as an intern. The turn lands
# because a fortune is supposed to promise a rise, and this one promises
# a rise followed immediately by a demotion nobody warned it about.
import os

LINE = "You will be retired with full honors, then quietly rebooted as an intern."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 140, "entry must be 1 to 140 characters"
assert len(LINE.encode("utf-8")) <= 140, "entry must be at most 140 bytes"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be a single sentence"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
