#2798 블랙잭
#브루트포스
N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_N, result = 0, 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      max_N = cards[i] + cards[j] + cards[k]
      if max_N <= M:
        result = max(max_N, result)
print(result)

#itertools 이용
#import itertools

#N, M = map(int, input().split())
#cards = list(map(int, input().split()))

# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합
#combi_sum = [sum(combi) for combi in itertools.combinations(cards, 3) if sum(combi) <= M]

# 최종 결과 : M에 최대한 가까운 카드 3장의 합
#print(max(combi_sum))
