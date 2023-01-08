x = int(input())
y = x
count = 0
while 1:
  c = ((y // 10) + (y % 10)) % 10
  y = ((y % 10) * 10) + c
  count = count + 1
  if x == y:
    break
print(count)
