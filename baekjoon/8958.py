T = int(input())
for _ in range(T):
  X = list(input())
  score = 0
  sum = 0
  for x in X:
    if x == 'O':
      score += 1
      sum += score
    else:
      score = 0
  print(sum)