import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())

  dp = [0] * (n + 1)
  dp[1] = 1 # 2x1 타일 1개로 고정
  dp[2] = 3 # 2x1 타일 2개 or 1x2 타일 2개 or 2x2 타일 1개

  for i in range(3, n + 1):
    # 'dp[i - 1]' 의미: dp[i - 1]에 2x1 타일 덧붙이기
    #   -> 경우의 수 1개
    # '(2 * dp[i - 2])' 의미: dp[i - 2]에 1x2 타일 2개 덧붙이기 or 2x2 타일 1개 덧붙이기
    #   -> 경우의 수 2개
    dp[i] = dp[i - 1] + (2 * dp[i - 2])

  print(dp[n] % 10007)
