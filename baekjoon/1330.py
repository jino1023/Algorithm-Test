data = list(map(int, input().split()))
if data[0] > data[1]:
  print(">")
elif data[0] < data[1]:
  print("<")
else:
  print("==")