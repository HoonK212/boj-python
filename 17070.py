import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  coordinates = [list(map(int, input().split())) for _ in range(n)]

  dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
  dp[0][0][1] = 1

  for i in range(2, n):
    if coordinates[0][i] == 0:
      dp[0][0][i] = dp[0][0][i - 1]
    elif coordinates[0][i] == 1:
      break

  for i in range(1, n):
    for j in range(1, n):
      if coordinates[i][j] == 0:
        dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
        dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
        if coordinates[i][j - 1] == 0 and coordinates[i - 1][j] == 0:
          dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

  print(dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1])
