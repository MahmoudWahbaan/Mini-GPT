import sys, math

# LayerNorm: y = (x - mean) / sqrt(var + eps).  Pre-norm style, gamma=1 beta=0.
# Parse EPS (default 1e-5) and any number of NORM lines; emit normalised rows.

EPS = 1e-5
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line:
        continue
    if line.startswith("EPS "):
        EPS = float(line[4:])
    elif line.startswith("NORM "):
        x = [float(v) for v in line[5:].split(",")]
        # TODO: compute mean, var, normalised y; print 4-decimal floats
        mean  = (sum(x))/(len(x))
        var = 0
        for num in x:
            var = var + (num-mean)**2
        var = var / len(x)
        for i in range(len(x)):
            y_i = round((x[i]-mean) / ((var+EPS)**0.5),4)
            if(i==(len(x)-1)):
                print("{:.4f}".format(y_i))
            else:
                print("{:.4f}".format(y_i),end = ',')


