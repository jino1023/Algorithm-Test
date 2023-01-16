chars = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
input_alpa = input()
t = 0
for i in chars:
  for j in i:
    for x in input_alpa:
      if j == x:
        t += chars.index(i) + 3
print(t)