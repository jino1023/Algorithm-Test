#7568 덩치
N = int(input())
people_list = []
for _ in range(N):
  w, h = map(int, input().split())
  people_list.append((w, h))
for i in people_list:
  r = 1
  for j in people_list:
    if i[0] < j[0] and i[1] < j[1]:
      r += 1
  print(r, end=" ")