n1, n2 = map(list, input().split())
n1.reverse()
n2.reverse()
a, b = "", ""
for i in range(3):
  a += n1[i]
  b += n2[i]
print(a if a > b else b)