#2775
T = int(input())
for i in range(T):
  #층
  k = int(input())
  #호실
  n = int(input())
  f = [i for i in range(1, n + 1)]
  for i in range(k):
    for j in range(1, n):
      f[j] += f[j - 1]
  print(f[n - 1])
