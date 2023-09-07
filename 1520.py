import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(x, y):

    # 목표 지점 도착
    if x == m - 1 and y == n - 1:
      return 1

    # 이미 방문한 지점
    if visited[x][y] != -1:
      return visited[x][y]

    # 방문 처리
    visited[x][y] = 0

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < m and 0 <= ny < n:
        if graph[x][y] > graph[nx][ny]:
          # visited[x][y]의 의미
          #   해당 지점부터 목표 지점까지 내리막길로 이동 가능한 경로의 개수
          visited[x][y] += dfs(nx, ny)

    return visited[x][y]

  m, n = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(m)]

  visited = [[-1] * n for _ in range(m)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  print(dfs(0, 0))
