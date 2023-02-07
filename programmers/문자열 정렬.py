# 문자열 정렬하기
# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성
def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) > 47 and ord(i) < 58:
            answer.append(int(i))
    return sorted(answer)