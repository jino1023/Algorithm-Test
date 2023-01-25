import sys
#지도의 크기
N = int(sys.stdin.readline())
graph = []
cnt = []
for i in range(N):
  graph.append(list(map(int, input())))


def dfs(x, y):
  #범위를 벗어나는 경우 종료
  if x <= -1 or x >= N or y <= -1 or y >= N:
    return False
  #현재 노드를 방문하지 않았다면
  if graph[x][y] == 1:
    #장애물 개수 체크
    cnt.append(1)
    #현재 노드 방문 처리
    graph[x][y] = 0
    #상하좌우의 위치를 재귀적으로 확인
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False


block = 0
blocks = []
for i in range(N):
  for j in range(N):
    if dfs(i, j) == True:
      block += 1
      #길이를 통해 장애물 개수 확인
      blocks.append(len(cnt))
      cnt = []
#총 블록의 수
print(block)
#장애물의 수 오름차순 정렬 후 출력
blocks.sort()
for i in blocks:
  print(i)
