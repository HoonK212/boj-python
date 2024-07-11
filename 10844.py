import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def count_stair_numbers(length):
    MOD = 1000000000

    # 계단 수를 저장하기 위한 DP 테이블 초기화
    # dp[i][j]: 길이가 i인 계단 수 중 마지막 자리가 j인 경우의 수
    dp = [[0] * 10 for _ in range(length + 1)]

    # 길이가 1인 경우 각 숫자별로 가능한 경우의 수 초기화 (0 제외)
    for i in range(1, 10):
      dp[1][i] = 1

    # 길이가 2 이상인 계단 수를 계산
    for i in range(2, length + 1):
      for j in range(10):
        if j == 0:
          # 마지막 자리가 0인 경우 이전 길이의 마지막 자리가 1이어야만 가능
          dp[i][j] = dp[i - 1][1]
        elif j == 9:
          # 마지막 자리가 9인 경우 이전 길이의 마지막 자리가 8이어야만 가능
          dp[i][j] = dp[i - 1][8]
        else:
          # 그 외의 숫자들은 이전 길이의 양쪽 인접 숫자에서 온다
          dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    # 최종 길이의 모든 계단 수 합계를 1,000,000,000으로 나눈 나머지를 반환
    return sum(dp[length]) % MOD


  # 입력받은 길이로 계단 수 계산
  n = int(input().strip())
  result = count_stair_numbers(n)
  print(result)