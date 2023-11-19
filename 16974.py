import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n, x = map(int, input().split())

  burger = [1] * 51
  patty = [1] * 51

  for i in range(1, n + 1):
    burger[i] = 2 * burger[i - 1] + 3
    patty[i] = 2 * patty[i - 1] + 1


  def eat(n, x):
    if n == 0:
      return x
    if x == 1:
      return 0
    elif x <= burger[n - 1] + 1:
      return eat(n - 1, x - 1)
    elif x == burger[n - 1] + 2:
      return patty[n - 1] + 1
    elif x <= 2 * burger[n - 1] + 2:
      return patty[n - 1] + 1 + eat(n - 1, (x - burger[n - 1] - 2))
    else:
      return patty[n]


  print(eat(n, x))
