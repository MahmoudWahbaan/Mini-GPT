import sys, math

# Numerically stable softmax.
# softmax(x_i) = exp(x_i - max(x)) / sum_j exp(x_j - max(x))
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line or not line.startswith("SOFTMAX "):
        continue
    x = [float(v) for v in line[8:].split(",")]
    # TODO: subtract max(x), exponentiate, normalise, print 4-decimal floats.
    s_x = []
    sum_exp_j = 0
    m = max(x)
    for i in range(len(x)):
        x[i] =  x[i] - m
    for j in x:
        sum_exp_j = sum_exp_j + math.exp(j)
    for i in range(len(x)):
        x_i = x[i]
        exp_xi = math.exp(x_i)
        s_x.append(round((exp_xi)/(sum_exp_j),4))
    for i in range(len(s_x)):
        if(i==(len(s_x)-1)):
            print("{:.4f}".format(s_x[i]))
        else:
            print("{:.4f}".format(s_x[i]),end = ',')   
        