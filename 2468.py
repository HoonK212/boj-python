import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  def bfs(x, y, h):
    global visited, dq, dx, dy, graph

    visited[x][y] = True
    dq.append((x, y))

    while dq:
      x, y = dq.pop()

      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
          visited[nx][ny] = True

          # 이동할 지점이 물에 잠기지 않는 경우만 deque에 append
          if graph[nx][ny] > h:
            dq.append((nx, ny))

  n = int(input())
  graph = []
  max_li = []

  for _ in range(n):
    graph.append(list(map(int, input().split())))
    max_li.append(max(graph[-1]))

  dq = deque()
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  ans_li = []

  for h in range(0, max(max_li)):
    visited = [[False] * n for _ in range(n)]
    ans = 0

    for i in range(n):
      for j in range(n):
        if visited[i][j] == False and graph[i][j] > h: # 물에 잠기지 않는 지점에서만 bfs 함수 실행 가능
          bfs(i, j, h)
          ans += 1

    ans_li.append(ans)

  print(max(ans_li))
