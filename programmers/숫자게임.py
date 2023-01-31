#숫자게임
def solution(A, B):
    answer = 0
    #내림차순으로 정렬
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in A:
        if i < B[0]:
            answer+=1
            del B[0]
        else:
            continue
    return answer