import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n = int(input())
  p = [0] + list(map(int, input().split()))
  dp = [0 for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(1, i + 1):
      dp[i] = max(dp[i], dp[i - j] + p[j])

  print(dp[i])
