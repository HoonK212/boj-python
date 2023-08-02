import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def mul(n, a, b):
    result = [[0] * n for _ in range(n)]
    for row in range(n):
      for col in range(n):
        for i in range(n):
          result[row][col] += a[row][i] * b[i][col]
        result[row][col] %= 1000
    return result


  def cal(n, b, a):
    if b == 1:
      return a
    elif b == 2:
      return mul(n, a, a)
    else:
      temp = cal(n, b // 2, a)
      if b % 2 == 0:
        return mul(n, temp, temp)
      else:
        return mul(n, mul(n, temp, temp), a)


  n, b = map(int, input().split())
  a = [[*map(int, input().split())] for _ in range(n)]

  result = cal(n, b, a)

  for row in result:
    for num in row:
      print(num % 1000, end=' ')
    print()
