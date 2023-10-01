import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  n = int(input())

  t = [0 for i in range(n + 1)]
  p = [0 for i in range(n + 1)]
  dp = [0 for i in range(n + 1)]

  for i in range(n):
    t[i], p[i] = map(int, input().split())

  # 뒤에서 부터 dp를 채우는 것이 핵심 !!!
  for i in range(len(t) - 2, -1, -1):
    if t[i] + i <= n:
      dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else:
      dp[i] = dp[i + 1] # 날짜가 초과하여 상담이 불가능한 경우

  print(dp[0])
