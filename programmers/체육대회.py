from itertools import permutations

def solution(ability):
    n = len(ability)
    m = len(ability[0])
    max_sum = 0
    
    for perm in permutations(range(n), m):
        sum_ability = sum([ability[i][j] for j, i in enumerate(perm)])
        max_sum = max(max_sum, sum_ability)
    
    return max_sum

# 테스트 코드
ability1 = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
ability2 = [[20, 30], [30, 20], [20, 30]]

print(solution(ability1))  # 210
print(solution(ability2))  # 60
