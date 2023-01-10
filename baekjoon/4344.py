C = int(input())
for _ in range(C):
  N = list(map(int, input().split()))
  avg = sum(N[1:]) / N[0]
  count = 0
  for s in N[1:]:
    if s > avg:
      count += 1
  r = count / N[0] * 100
  print(f"{r:.3f}%")