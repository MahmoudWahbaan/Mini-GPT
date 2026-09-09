import sys, math

# Scaled dot-product attention scores: Q @ K^T / sqrt(D).
# Parse 'T <T> D <D>', then T rows of Q, then T rows of K.
# Emit the T x T score matrix, 4 decimals.

# TODO: implement the dot product and the /sqrt(D) scaling.

line = input().split()
T = int(line[1])
D = int(line[-1])
Query = []
Key = []
for i in range(T):
  line = input().split(',')
  vec = []
  for i in range(len(line)):
    vec.append(int(line[i]))
  Query.append(vec)
for i in range(T):
  line = input().split(',')
  vec = []
  for i in range(len(line)):
    vec.append(int(line[i]))
  Key.append(vec)
Attention  = []
s_d = math.sqrt(D)
for i in range(T):
  mat1 = Query[i]
  res = []
  for j in range(T):
    mat2 = Key[j]  
    calc = 0
    for dim in range(D):
      calc = calc+((mat1[dim]*mat2[dim])/(s_d))
    res.append(round(calc,4))
  Attention.append(res)

for row in Attention:
  for i in range(len(row)):
    if(i==(len(row)-1)):
      print("{:.4f}".format(row[i]))
    else:
      print("{:.4f}".format(row[i]),end = ',')