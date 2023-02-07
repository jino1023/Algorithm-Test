# 예산
# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in range(len(d)):
        if sum+d[i] <= budget:
            sum+=d[i]
            answer+=1
        else:
            break
    return answer