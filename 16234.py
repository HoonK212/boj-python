import sys; input = sys.stdin.readline
import math
from collections import deque
if __name__ == '__main__':

  def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    union = [(i, j)]
    cnt = coordinates[i][j]

    while queue:
      x, y = queue.popleft()
      for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
          continue
        if visited[nx][ny]:
          continue
        if l <= abs(coordinates[nx][ny] - coordinates[x][y]) <= r:
          queue.append((nx, ny))
          visited[nx][ny] = True
          union.append((nx, ny))
          cnt += coordinates[nx][ny]

    for x, y in union:
      coordinates[x][y] = math.floor(cnt / len(union))

    return len(union)

  n, l, r = map(int, input().split())
  coordinates = []
  for i in range(n):
    coordinates.append(list(map(int, input().split())))

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  result = 0
  while 1:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
      for j in range(n):
        if not visited[i][j]:
          if bfs(i, j) > 1:
            flag = True
    if not flag:
      break
    result += 1

  print(result)
