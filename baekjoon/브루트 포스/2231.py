#2231 분해합
N = int(input())
for i in range(1, N + 1):
  # i의 각 자리수를 더함
  x = sum(map(int, str(i)))
  # 분해합 = 생성자 + 각 자릿수의 합
  y = i + x
  # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을떄가 가장 작은 생성자를 가짐
  if y == N:
    print(i)
    break
  # 생성자 i와 입력값 N이 같다는 것은 생성자가 없다는 뜻
  if i == N:
    print(0)