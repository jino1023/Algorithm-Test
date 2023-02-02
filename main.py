#멀쩡한 사각형
#교점 수=반복되는 횟수=(최대공약수)
#교점이 없을 때 대각선이 뚫는 사각형 개수=(가로'+세로'-1)/ (가로'+세로'-1)*(최대공약수)=(가로+세로-최대공약수)
import math
def solution(w,h):
    answer = (w * h) - ((w + h) - math.gcd(w,h))
    return answer