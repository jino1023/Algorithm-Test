cl = []
for _ in range(10):
  i = int(input())
  j = i % 42
  if j not in cl:
    cl.append(j)
print(len(cl))