import sys, math

# Causal mask + softmax.
# Read 'T <T>' and T rows of T floats each.  For row i, set entries j>i to -inf,
# then softmax (numerically stable).  Print T rows of T floats (4 decimals).

# TODO: implement.

line = input().split()
t = int(line[-1])
mat = []
for i in range(t):
  row = []
  nums = input().split(',')
  for j in range(t):
    row.append(float(nums[j]))
  mat.append(row)
for i in range(t):
  for j in range(i+1,t):
    mat[i][j] = -1*math.inf
for row in range(t):
  sum_e = 0
  for col in range(t):
    sum_e = sum_e + math.exp(mat[row][col])
  for col in range(t):
    mat[row][col] = (math.exp(mat[row][col]))/(sum_e)
for r in range(t):
  for c in range(t):
    if(c == t-1):
      print("{:.4f}".format(mat[r][c]))
    else:
      print("{:.4f}".format(mat[r][c]),end = ',')