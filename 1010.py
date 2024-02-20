import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def factorial(num):
    result = 1
    for i in range(1, num + 1):
      result *= i
    return result


  t = int(input())
  for _ in range(t):
    n, m = map(int, input().split())
    answer = factorial(m) // (factorial(n) * factorial(m - n))
    print(answer)