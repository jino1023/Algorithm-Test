# 1193 분수찾기
# '1/1','1/2,2/1','3/1,2/2,1/3','1/4,2/3,3/2,4/1'
# X가 몇 번째 줄,숫자인지 구하고
# 짝수번 째 줄인지 홀수번 째 줄인지에 따라 분자,분모의 증감방향이
# 홀수번째는 분자는 1씩 작아지고 분모는 1씩 증가함, 짝수번째는 반대로
X = int(input())
line = 1
while X > line:
  X -= line
  line += 1
if (line % 2) == 0:
  n = X
  d = line - X + 1
else:
  n = line - X + 1
  d = X
print(f'{n}/{d}')