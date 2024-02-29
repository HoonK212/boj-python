import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(y, x):
    if x < 0 or x >= w or y < 0 or y >= h:
      return False

    if coordinates[y][x] == 1:
      coordinates[y][x] = 0

      dfs(y - 1, x)
      dfs(y + 1, x)
      dfs(y, x - 1)
      dfs(y, x + 1)

      dfs(y - 1, x - 1)
      dfs(y - 1, x + 1)
      dfs(y + 1, x - 1)
      dfs(y + 1, x + 1)
      return True
    return False


  while True:
    w, h = map(int, input().split())

    if w == 0 & h == 0:
      break

    coordinates = []
    for _ in range(h):
      coordinates.append(list(map(int, input().split())))

    answer = 0
    for i in range(h):
      for j in range(w):
        if dfs(j, i):
          answer += 1
    print(answer)