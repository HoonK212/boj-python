import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(x, y):
    global cnt

    if x < 0 or x >= m or y < 0 or y >= n:
      return 0

    if coordinates[x][y] == 1:
      return 0

    coordinates[x][y] = 1
    cnt += 1

    for i in range(4):
      dfs(x + dx[i], y + dy[i])

    return cnt


  m, n, k = map(int, input().split())
  coordinates = [[0] * n for _ in range(m)]

  for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
      for j in range(x1, x2):
        coordinates[i][j] = 1

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  cnt = 0
  result = []

  for i in range(m):
    for j in range(n):
      cnt = dfs(i, j)
      if cnt:
        result.append(cnt)
        cnt = 0

  result.sort()
  print(len(result))
  for i in result:
    print(i, end=' ')
