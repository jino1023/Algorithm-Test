N = int(input())
X = list(map(int, input().split()))
M = max(X)
for i in range(N):
  X[i] = X[i] / M * 100
print(sum(X) / N)
