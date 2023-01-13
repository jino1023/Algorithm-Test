l = input().upper()
il = list(set(l))
cl = []
for i in il:
  cl.append(l.count(i))
if cl.count(max(cl)) >= 2:
  print("?")
else:
  print(il[cl.index(max(cl))])