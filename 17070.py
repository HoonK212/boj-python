import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  coordinates = [list(map(int, input().split())) for _ in range(n)]

  # 가로, 세로, 대각선의 이동을 각각 이차원 배열로 계산 가능하도록 3차원 배열을 생성하는 것이 핵심 !!!
  dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

  # 첫 행의 이동은 가로로 이동하는 경우에만 가능
  dp[0][0][1] = 1
  for i in range(2, n):
    if coordinates[0][i] == 0:
      dp[0][0][i] = dp[0][0][i - 1]
    elif coordinates[0][i] == 1:
      break

  # (1, 1)부터 (n, n)까지 계산
  #   첫 행은 위에서 이미 계산 & 첫 열은 이동 불가능
  for i in range(1, n):
    for j in range(1, n):
      # 벽의 유무 고려 (가로, 세로 이동)
      if coordinates[i][j] == 0:
        # 가로, 세로 이동 계산
        dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1] # 앞서 세로로 이동한 경우 -> 가로 이동 불가능
        dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j] # 앞서 가로로 이동한 경우 -> 세로 이동 불가능
        # 벽의 유무 고려 (대각선 이동)
        if coordinates[i][j - 1] == 0 and coordinates[i - 1][j] == 0:
          dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1] # 앞선 이동과 관계 없이 대각선 이동 가능

  # 가로, 세로, 대각선 이동에 대한 각 연산의 합 출력
  print(dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1])
