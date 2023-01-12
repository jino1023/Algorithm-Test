S = input()
alpa = 'abcdefghijklmnopqrstuvwxyz'
for i in alpa:
  if i in S:
    print(S.index(i), end=" ")
  else:
    print('-1', end=" ")