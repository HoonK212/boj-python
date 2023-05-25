import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import deque
if __name__ == '__main__':

  def bfs():
    q = deque()
    q.append((start_x, start_y))

    while q:
      x, y = q.popleft()

      if x == end_x and y == end_y:
        return coordinates[x][y] - 1

      # 미리 정의한 나이트의 움직임에 따라 range(8)로 반복문 실행
      for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < l and 0 <= ny < l and coordinates[nx][ny] == 0:
          coordinates[nx][ny] = coordinates[x][y] + 1
          q.append((nx, ny))

  # 가능한 나이트의 모든 움직임을 미리 좌표로 정의
  dx = [-1, 1, 2, 2, 1, -1, -2, -2]
  dy = [2, 2, 1, -1, -2, -2, -1, 1]

  t = int(input())
  for _ in range(t):
    l = int(input())

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    # 한 변의 길이 l에 따라 2차원 배열 생성
    coordinates = [[0] * l for _ in range(l)]
    coordinates[start_x][start_y] = 1

    print(bfs())
