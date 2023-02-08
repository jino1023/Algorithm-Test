# 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    used_words=[]
    for i in range(len(words)):
        if i == 0:
            used_words.append(words[i])
        else:
            if words[i] in used_words or words[i][0] != words[i-1][-1]:
                return [(i%n)+1,(i//n)+1]
            used_words.append(words[i])
    return [0, 0]