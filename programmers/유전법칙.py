def bean(generation, idx):
  # 첫번째 세대의 경우 Rr로 고정
  if generation == 1:
    return "Rr"

  # 부모에서 유전되는 유전자 결정
  parent = bean(generation - 1, (idx - 1) // 4 + 1)

  # 부모의 유전자 결정에 따라 유전자 계산
  if parent == "RR" or parent == "rr":
    return parent
  group = (idx - 1) % 4
  if group == 0:
    return "RR"
  elif group == 1 or group == 2:
    return "Rr"
  else:
    return "rr"


def solution(queries):
  answer = []
  for query in queries:
    ans = bean(query[0], query[1])
    answer.append(ans)
  return answer


"""
def bean(generation, idx):
    # 첫번째 세대의 경우 Rr로 고정
    if generation == 1:
        return "Rr"
    
    # 이미 계산된 유전자인 경우 바로 반환
    if (generation, idx) in cache:
        return cache[(generation, idx)]
    
    # 부모에서 유전되는 유전자 결정
    parent = bean(generation - 1, (idx - 1) // 4 + 1)
    
    # 부모의 유전자 결정에 따라 유전자 계산
    if parent == "RR" or parent == "rr":
        gene = parent
    else:
        group = (idx - 1) % 4
        if group == 0:
            gene = "RR"
        elif group == 1 or group == 2:
            gene = "Rr"
        else:
            gene = "rr"
    
    # 계산된 유전자를 저장하고 반환
    cache[(generation, idx)] = gene
    return gene

def solution(queries):
    answer = []
    for query in queries:
        ans = bean(query[0], query[1])
        answer.append(ans)
    return answer

cache = {}
"""
print(solution([[3, 5]]))
print(solution([[3, 8], [2, 2]]))
print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))
