import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

# 트리 생성
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# BFS 탐색
queue = deque([1])
while queue:
    node = queue.popleft()
    for child in tree[node]:
        if parents[node] != child:
            parents[child] = node
            queue.append(child)

# 결과 출력
for i in range(2, n + 1):
    print(parents[i])
