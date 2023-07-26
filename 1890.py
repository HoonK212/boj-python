import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  coordinates = [list(map(int, input().split())) for _ in range(n)]
  dp = [[0] * n for _ in range(n)]
  dp[0][0] = 1

  for x in range(n):
    for y in range(n):
      if x == y == n - 1:
        break

      distance = coordinates[x][y]
      if x + distance < n:
        dp[x + distance][y] += dp[x][y]
      if y + distance < n:
        dp[x][y + distance] += dp[x][y]

  print(dp[n - 1][n - 1])
