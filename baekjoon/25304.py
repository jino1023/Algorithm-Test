total = int(input())
i = int(input())
sum = 0
for i in range(1, i + 1):
  a, b = map(int, input().split())
  sum = sum + (a * b)
if total == sum:
  print("Yes")
else:
  print("No")