import sys, math

# Two pre-norm residual sublayers with identity sublayer:
#   y1 = x + alpha * LayerNorm(x)
#   y2 = y1 + alpha * LayerNorm(y1)
# Use eps=1e-5, gamma=1, beta=0.

EPS = 1e-5
ALPHA = 0

def layer_norm(v):
    # TODO: implement (mean, var, normalise)
    tmp_v = []
    mean =  (sum(v))/(len(v))
    var = (sum(((vi-mean)**2) for vi in v))/(len(v))
    for vi in v:
        tmp_v.append(ALPHA * ((vi-mean)/math.sqrt(var+EPS)))
    for i in range(len(v)):
        v[i] = v[i] + tmp_v[i]
    return v

# parse X and ALPHA, then compute y1, y2, print y2 with 4 decimals.
line = input().rstrip().split()
line = line[-1].split(',')
X = []
for i in range(len(line)):
    X.append(float(line[i]))
ALPHA = float(input().split()[-1])

y1 = layer_norm(X)
y2 = layer_norm(y1)

for i in range(len(y2)):
    if(i== (len(y2)-1)):
        print("{:.4f}".format(y2[i]))
    else:
        print("{:.4f}".format(y2[i]),end=',')