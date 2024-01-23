import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from math import sqrt
if __name__ == '__main__':

  def get_c(mid):
    a = sqrt(x ** 2 - mid ** 2)
    b = sqrt(y ** 2 - mid ** 2)
    return a * b / (a + b)


  x, y, c = map(float, input().split())
  start, end = 0, min(x, y)

  answer = 0
  while end - start > 1e-6:
    mid = (start + end) / 2
    if get_c(mid) >= c:
      answer = mid
      start = mid
    else:
      end = mid

  print("{}".format(round(answer, 4)))