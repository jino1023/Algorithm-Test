A, B = map(int, input().split())
C = int(input())
H = (B + C) // 60
M = (B + C) % 60

if (B + C) >= 60:
  if A + H >= 24:
    A = A - 24
  A = A + H
  print(A, M)
else:
  if (A >= 24):
    A = A - 24
  print(A, M)
