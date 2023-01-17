#2292 벌집
N = int(input())
H = 1
cnt = 1
while N > H:
  H += 6 * cnt
  cnt += 1
print(cnt)