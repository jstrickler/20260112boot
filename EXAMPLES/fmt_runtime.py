FIRST_NAME = 'Fred'
LAST_NAME = 'Flintstone'
AGE = 35

print(f"{FIRST_NAME} {LAST_NAME}")

WIDTH = 12
print(f"[{FIRST_NAME:{WIDTH}s}] [{LAST_NAME:{WIDTH}s}]")  # value of WIDTH used in format spec

PAD = '-'
WIDTH = 16
ALIGNMENTS = ('<', '>', '^')

for ALIGNMENT in ALIGNMENTS:
    print(f"{FIRST_NAME:{PAD}{ALIGNMENT}{WIDTH}s} {LAST_NAME:{PAD}{ALIGNMENT}{WIDTH}s}")  # values of PAD, WIDTH, ALIGNMENTS used in format spec
