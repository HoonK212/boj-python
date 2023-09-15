import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def move(n, a, b, c):

    if n == 1:
      print(a, c)
      return

    move(n - 1, a, c, b)
    print(a, c)
    move(n - 1, b, a, c)

  n = int(input())

  cnt = 2 ** n - 1
  print(cnt)

  move(n, 1, 2, 3)
