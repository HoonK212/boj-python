import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def recursion(i, j, size):
    if size == 3:
      for di in range(3):
        for dy in range(di + 1):
          stars[i + di][j - dy] = stars[i + di][j + dy] = "*"
      stars[i + 1][j] = " "
      return

    n = size // 2
    recursion(i, j, n)
    recursion(i + n, j - n, n)
    recursion(i + n, j + n, n)

  n = int(input())
  stars = [[" " for _ in range(n * 2)] for _ in range(n)]

  recursion(0, n - 1, n)

  for star in stars:
    print("".join(star))
