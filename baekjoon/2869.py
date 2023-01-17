#2869 달팽이는 올라가고 싶다
import sys

A, B, V = map(int, sys.stdin.readline().split())
# 도달하는 날을 d라고 할 떄, 총 올라가는 횟수는 d, 내려오는 횟수는 d-1번
# A*d - B*(d-1) = V
# d = (V-B)/(A-B)
d = (V - B) / (A - B)
print(int(d) if d == int(d) else int(d) + 1)