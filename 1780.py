import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(x, y, z):
    global answer
    visited = coordinates[x][y]

    for i in range(x, x + z):
      for j in range(y, y + z):
        if coordinates[i][j] != visited:
          for k in range(3):
            for l in range(3):
              dfs(x + k * z // 3, y + l * z // 3, z // 3)
          return

    if visited == -1:
      answer[0] += 1
    elif visited == 0:
      answer[1] += 1
    else:
      answer[2] += 1


  n = int(input())
  coordinates = [list(map(int, input().split())) for _ in range(n)]

  answer = [0, 0, 0]
  dfs(0, 0, n)

  [print(ans) for ans in answer]
