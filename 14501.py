import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  n = int(input())
  t, p, dp = [0 for i in range(n + 1)], [0 for i in range(n + 1)], [0 for i in range(n + 1)]
  for i in range(n):
    t[i], p[i] = map(int, input().split())

  for i in range(len(t) - 2, -1, -1):
    if t[i] + i <= n:
      dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else:
      dp[i] = dp[i + 1]

  print(dp[0])
