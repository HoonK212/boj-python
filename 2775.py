import sys; input = sys.stdin.readline
if __name__ == '__main__':

  t = int(input())
  answer = []

  for _ in range(t):
    k, n = int(input()), int(input())

    dp = [[0 for _ in range(n)] for _ in range(k + 1)]

    for i in range(k + 1):
      for j in range(n):
        if i==0:
          dp[i][j] = j + 1
        else:
          for l in range(j + 1):
            dp[i][j] += dp[i - 1][l]

    answer.append(dp[k][n - 1])

  print(*answer, sep="\n")
