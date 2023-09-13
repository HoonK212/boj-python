import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def recursion(num, i):
    global answer

    if i ** 2 > num:
      answer.append(num)
      return

    if num % i == 0:
      answer.append(i)
      recursion(num // i, i)
    else:
      recursion(num, i + 1)

  n = int(input())

  if n == 1:
    exit()

  answer = []
  recursion(n, 2)

  print(*answer, sep="\n")
