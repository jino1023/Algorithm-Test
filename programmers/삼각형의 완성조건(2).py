#삼각형의 완성조건(2)
#가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야함
def solution(sides):
    answer = 0
    #기존요소 중 가장 긴 변이 있다면
    # X + min(sides) > max(sides)
    # X > max(sides) - min(sides)
    #나머지 한 변이 가장 긴 변이라면
    # X < sum(sides)
    # max(sides) - min(sides) < X < sum(sides)
    answer = sum(sides) - (max(sides) - min(sides)) - 1
    return answer