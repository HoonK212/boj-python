import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  answer = [1, 1]

  # 피보나치 수열 계산
  for _ in range(n - 2):
    answer.append(answer[-2] + answer[-1])

  print(answer[-1])
  