import sys

# Embedding table lookup.
# Read VOCAB <V> DIM <D>, then V rows of floats, then TOKENS ids.
# Emit one row of comma-separated floats per token id (4 decimals).
# Out-of-range ids -> D zeros.

# TODO: parse the input and print the looked-up rows.
IN = input("")

TEMP = IN.split()
VOCAB  = int(TEMP[1])
DIM = int(TEMP[-1])

lookup = {}

for i in range(VOCAB):
  embedds = input()
  embedds = embedds.split(',')
  for j in range(len(embedds)):
    embedds[j] =float(embedds[j])
  lookup[i] = embedds
TOKENS = input("")
TOKENS = TOKENS.split()
TOKENS = TOKENS[-1]
TOKENS = TOKENS.split(',')
for token in TOKENS:
  token = int(token)
  embedd = lookup.get(token,[float(0) for i in range(DIM)])
  for i in range(DIM):
    if(i == DIM-1):
      print("{:.4f}".format(embedd[i]))
    else:
      print("{:.4f}".format(embedd[i]),end=',')