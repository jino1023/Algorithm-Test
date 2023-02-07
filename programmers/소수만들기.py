# 소수만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for combination in combinations(nums, 3):
        if is_prime(sum(combination)):
            answer += 1
    return answer
