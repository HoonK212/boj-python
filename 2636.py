import sys; input = sys.stdin.readline;
from collections import deque
if __name__ == '__main__':

  def bfs():
    queue = deque()
    queue.append([0, 0])

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    cnt = 0
    while queue:
      x, y = queue.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
          if coordinates[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append([nx, ny])
          elif coordinates[nx][ny] == 1:
            coordinates[nx][ny] = 0
            visited[nx][ny] = 1
            cnt += 1

    answer.append(cnt)
    return cnt

  n, m = map(int, input().split())
  coordinates = []
  for i in range(n):
    coordinates.append(list(map(int, input().split())))

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  time = 0
  answer = []

  while 1:
    time += 1

    if bfs() == 0:
      break

  print(time - 1)
  print(answer[-2])
