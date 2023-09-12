import sys; input = sys.stdin.readline
from itertools import permutations
if __name__ == '__main__':

  n, k = map(int, input().split())
  kits = list(map(int, input().split()))

  # 입력받은 운동 키트로 순열 리스트 생성
  permutations = list(permutations(kits, n))

  # 생성된 순열 리스트의 길이로 answer 초기화
  answer = len(permutations)

  # 순열 리스트에서 각각의 경우를 계산
  for p in permutations:
    mass_sum = 500
    for i in range(n):
      mass_sum += p[i] - k

      # 3대 중량 합이 500 밑으로 떨어지는 경우를 answer에서 제외
      if mass_sum < 500:
        answer -= 1
        break

  print(answer)
