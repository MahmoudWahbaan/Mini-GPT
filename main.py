import sys

# Character-level tokenizer.
# Parse the ALPHABET line, build a char -> index map,
# then map every char of the TEXT line. Missing chars -> -1.
alphabet = ""
text = ""
for raw in sys.stdin:
    line = raw.rstrip("\n")
    if line.startswith("ALPHABET "):
        alphabet = line[len("ALPHABET "):]
    elif line.startswith("TEXT "):
        text = line[len("TEXT "):]

# TODO: build the alphabet->index map and emit comma-separated ids.

char_to_idx = {}
for c, i in enumerate(alphabet):
    char_to_idx[i] = c

for i in range(len(text)):
    print(char_to_idx.get(text[i], -1), end="," if i < len(text) - 1 else "")