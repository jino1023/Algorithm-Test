#https://school.programmers.co.kr/learn/courses/15007/lessons/121682
def solution(n, board, position):
  # 이웃을 구하기 위한 상대적 위치
  dx = [-1, -1, -1, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, -1, 1, -1, 0, 1]

  # 새로운 보드를 초기화
  next_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
  for i in range(len(board))
  # 각 칸을 순회하며 새로운 상태를 계산
  for i in range(len(board)):
    for j in range(len(board[0])):
      # 현재 칸의 이웃을 구함
      cnt = 0
      for k in range(8):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < len(board) and 0 <= ny < len(
            board[0]) and board[nx][ny] == 1:
          cnt += 1
      # 살아있는 경우
      if board[i][j] == 1:
        # 살아있는 칸 주변에 이웃이 2명 이하 존재하면 그 칸은 다음 세대에 죽는다
        # 살아있는 칸 주변에 이웃이 5명 이상 존재하면 그 칸은 다음 세대에 죽는다
        if cnt <= 2 or cnt >= 5:
          next_board[i][j] = 0
        else:
          next_board[i][j] = 1
      # 죽어있는 경우
      else:
        # 죽어있는 칸 주변에 이웃이 정확히 2명 존재하면 그 칸은 다음 세대에 살아난다.
        if cnt == 2:
          next_board[i][j] = 1

  # 결과를 반환
  return [next_board[pos[0]][pos[1]] for pos in position]
