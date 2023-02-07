# 배달
# https://school.programmers.co.kr/learn/courses/30/lessons/12978
from collections import defaultdict
from queue import Queue

def solution(N, road, K):
    # 각 마을을 연결하는 도로의 정보를 저장할 dictionary 생성
    graph = defaultdict(list)
    for r in road:
        u, v, w = r
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # BFS 를 위한 큐 생성
    q = Queue()
    q.put(1)
    
    # 1번 마을에서 각 마을까지의 거리를 저장할 dictionary 생성
    dist = {i: float('inf') for i in range(1, N + 1)}
    dist[1] = 0
    
    # BFS
    while not q.empty():
        u = q.get()
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                q.put(v)
    
    # 음식 배달이 가능한 마을의 개수를 세어 return
    cnt = 0
    for i in range(1, N + 1):
        if dist[i] <= K:
            cnt += 1
    return cnt
