import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def check():
    for i in range(n):
      tmp = i
      for j in range(h):
        if graph[j][tmp]:
          tmp += 1
        elif tmp > 0 and graph[j][tmp - 1]:
          tmp -= 1
      if tmp != i:
        return False
    return True


  def dfs(x, y, cnt):
    global answer
    if answer <= cnt:
      return
    if check():
      answer = min(answer, cnt)
      return
    if cnt == 3:
      return
    for i in range(x, h):
      k = y if i == x else 0
      for j in range(k, n - 1):
        if graph[i][j] == 0:
          graph[i][j] = 1
          dfs(i, j + 2, cnt + 1)
          graph[i][j] = 0


  n, m, h = map(int, sys.stdin.readline().split())
  graph = [[0] * n for _ in range(h)]

  for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1

  answer = 4
  dfs(0, 0, 0)
  print(answer if answer <= 3 else -1)
