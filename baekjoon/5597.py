a = []
for i in range(1, 31):
  a.append(i)
for j in range(1, 29):
  I = int(input())
  a.remove(I)
print(min(a))
print(max(a))
#for i in a:
#  if i not in b:
#    c.append(i)