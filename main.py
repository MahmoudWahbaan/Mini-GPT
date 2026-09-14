import sys

# Each transformer block preserves (B, T, D). The full stack of N layers also
# preserves it. Attention has Q, K, V and an output projection -> 4 * D^2 per
# layer. Emit the shape and that param count.

for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line or not line.startswith("SHAPE "):
        continue
    # TODO: parse B T D N_LAYERS and print "B T D params=<count>"
    line = line.split()
    print("{} {} {} params={}".format(int(line[1]),int(line[2]),int(line[3]),4*(int(line[3])**2)*int(line[-1])))
