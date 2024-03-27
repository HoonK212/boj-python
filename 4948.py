import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import math
if __name__ == '__main__':

  def count_primes(limit):
    is_prime = [True] * (limit + 1) # 소수 여부를 저장할 리스트 초기화 (기본적으로 모든 수를 소수로 가정)
    is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체
    for num in range(2, int(math.sqrt(limit)) + 1):
      if is_prime[num]:
        # num이 소수라면, num의 배수들은 소수가 아님 (num^2 미만의 배수는 이미 처리되었으므로 확인할 필요가 없음)
        for multiple in range(num * num, limit + 1, num):
          is_prime[multiple] = False

    # 소수의 개수를 합산하여 반환
    return sum(is_prime)


  while True:
    n = int(input())
    if n == 0:
      break

    # n보다 크고 2n보다 작거나 같은 소수의 개수 계산
    result = count_primes(2 * n) - count_primes(n)
    print(result)
