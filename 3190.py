import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import deque
if __name__ == '__main__':

  n = int(input())
  k = int(input())
  board = [[0] * (n + 1) for _ in range(n + 1)]
  board[1][1] = 1  # 뱀: 1

  for _ in range(k):
    row, col = map(int, input().split())
    board[row][col] = 2  # 사과: 2

  l = int(input())
  commands = {}
  for _ in range(l):
    sec, dir = input().split()
    commands[int(sec)] = dir

  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위 (시계 방향 순)
  current_direction = 0  # 뱀 초기 방향: 오른쪽

  snake = deque([(1, 1)])  # 뱀 초기 위치: 좌상단 출발
  time = 0  # 게임 시간

  while True:
    head_x, head_y = snake[-1]  # 뱀의 머리 위치
    dx, dy = directions[current_direction]
    nx, ny = head_x + dx, head_y + dy  # 다음 위치

    # 벽이나 자기자신의 몸과 부딪히면 게임 종료
    if nx <= 0 or ny <= 0 or nx > n or ny > n or (nx, ny) in snake:
      time += 1
      break

    # 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비움
    if board[nx][ny] != 2:
      tail_x, tail_y = snake.popleft()
      board[tail_x][tail_y] = 0

    # 뱀 이동
    snake.append((nx, ny))
    board[nx][ny] = 1
    time += 1

    # 방향 변환 시점이라면, 방향 전환 실행
    if time in commands:
      if commands[time] == 'D':
        current_direction = (current_direction + 1) % 4
      else:  # 'L'
        current_direction = (current_direction - 1) % 4

  print(time)
