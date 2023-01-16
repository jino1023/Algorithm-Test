#1712 손익분기점
#A=고정비용, B=가변비용, C=가격
A, B, C = map(int, input().split())
#가변비용이 물건가격보다 크거나 같은경우(손익분기점이 존재하지않음)
if B >= C:
  print('-1')
else:
  print(A // (C - B) + 1)