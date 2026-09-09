import sys, math

# Sinusoidal positional encoding.
# For each "PE <pos> <d_model>" line emit d_model floats:
#   even dim -> sin(pos / 10000^(2k/d_model))
#   odd dim  -> cos(pos / 10000^(2k/d_model))
# Round to 4 decimals.

for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line or not line.startswith("PE "):
        continue
    line = line.split()
    pos = int(line[1])
    d_model = int(line[-1])
    # TODO: parse pos, d_model and emit the comma-separated encoding.
    PE = []
    for k in range(d_model//2):
        PE.append( round(math.sin(pos/10000 ** ((2*k)/(d_model))),4))
        PE.append(round(math.cos(pos/10000 ** ((2*k)/(d_model))),4))
    for i in range(len(PE)):
        if((i==(len(PE)-1))):
            print("{:.4f}".format(PE[i]))
        else:
            print("{:.4f}".format(PE[i]),end=',') 