import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def recursion(num, i):
    global answer

    # i의 제곱이 num보다 크면 더 이상 반복하지 않는 것이 핵심 !!!
    if i ** 2 > num:
      answer.append(num)
      return

    if num % i == 0:
      answer.append(i)
      recursion(num // i, i)
    else:
      recursion(num, i + 1)

  n = int(input())

  # n이 1인 경우 아무것도 출력하지 않고 exit() 실행
  if n == 1:
    exit()

  answer = []
  recursion(n, 2)

  print(*answer, sep="\n")
