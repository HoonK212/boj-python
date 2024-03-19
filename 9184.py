import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  # 동적 프로그래밍을 통해 w(a, b, c)의 결과를 저장할 3차원 리스트 dp를 생성하고, 모든 원소를 1로 초기화 (인덱스 범위는 0에서 20까지로 설정)
  dp = [[[1 for x in range(21)] for y in range(21)] for z in range(21)]

  # 반복의 기준이 되는 차원의 순서에 주의
  for z in range(1, 21):
    for y in range(1, 21):
      for x in range(1, 21):
        if x < y < z: # a < b < c인 경우, w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)로 값을 변경
          dp[x][y][z] = dp[x][y][z - 1] + dp[x][y - 1][z - 1] - dp[x][y - 1][z]
        else: # 그 외의 경우, w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)로 값을 변경
          dp[x][y][z] = dp[x - 1][y][z] + dp[x - 1][y - 1][z] + dp[x - 1][y][z - 1] - dp[x - 1][y - 1][z - 1]

  while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: # 입력된 값이 모두 -1인 경우, 루프 종료
      break
    elif a <= 0 or b <= 0 or c <= 0: # a, b, c 중 하나라도 0 이하인 경우, "w(a, b, c) = 1"을 출력
      print("w({0}, {1}, {2}) = 1".format(a, b, c))
    elif a > 20 or b > 20 or c > 20: # a, b, c 중 하나라도 20을 초과하는 경우, 사전에 계산된 w(20, 20, 20)의 값인 1048576을 출력
      print("w({0}, {1}, {2}) = 1048576".format(a, b, c))
    else: # 그 외의 경우, dp 리스트에서 해당하는 값을 찾아 출력
      print("w({0}, {1}, {2}) = {3}".format(a, b, c, dp[a][b][c]))