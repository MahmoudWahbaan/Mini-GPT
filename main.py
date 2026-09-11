import sys

# Position-wise FFN: y = W2 @ relu(W1 @ x + b1) + b2
# Parse D, H, then X, W1, B1, W2, B2.

D = H = 0
X = []; W1 = []; B1 = []; W2 = []; B2 = []
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line: continue
    if(line[0] == 'D'):
        parts = line.split()
    elif(line[0] == 'X'):
        parts = line[2:].split(',')
    else:
        parts = line[3:].split(',')
    # parse the keyword lines above
    if(line[0] == 'D'):
        D=int(parts[1])
        H=int(parts[-1])
    elif(line[0] == 'X'):
        for i in range(0,len(parts)):
            X.append(float(parts[i]))
    elif(line[0:2] == 'W1'):
        for i in range(0,len(parts)):
            W1.append(float(parts[i]))
    elif(line[0:2] == 'W2'):
        for i in range(0,len(parts)):
            W2.append(float(parts[i]))
    elif(line[0:2] == 'B1'):
        for i in range(0,len(parts)):
            B1.append(float(parts[i]))
    elif(line[0:2] == 'B2'):
        for i in range(0,len(parts)):
            B2.append(float(parts[i]))


# TODO: compute hidden = relu(W1 @ X + B1), then y = W2 @ hidden + B2.
# Print y as 4-decimal comma-separated floats.
Layer1 = []
for j in range(H):
    value = 0
    for i in range(D):
        value = value + X[i] * W1[(j*D)+i]
    Layer1.append(value)

for i in range(H):
    Layer1[i] = max(0,Layer1[i]+B1[i])
Layer2 = []

for j in range(D):
    value = 0
    for i in range(H):
        value = value + Layer1[i] * W2[(j*H)+i]
    Layer2.append(value)

for i in range(D):
    Layer2[i] = Layer2[i]+B2[i]


for i in range(D):
    if(i==D-1):
        print("{:.4f}".format(Layer2[i]))
    else:
        print("{:.4f}".format(Layer2[i]),end = ',')
