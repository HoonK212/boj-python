import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(x, y):

    if x == m - 1 and y == n - 1:
      return 1

    if visited[x][y] != -1:
      return visited[x][y]

    visited[x][y] = 0

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < m and 0 <= ny < n:
        if graph[x][y] > graph[nx][ny]:
          visited[x][y] += dfs(nx, ny)

    return visited[x][y]

  m, n = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(m)]

  visited = [[-1] * n for _ in range(m)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  print(dfs(0, 0))
