import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def move(n, a, b, c):

    if n == 1:
      # a에서 c로 이동
      print(a, c)
      return

    # n - 1개의 원반을 기둥 a(시작 기둥 1)에서, c(목표 기둥 3)를 사용하여 b(보조 기둥 2)로 이동
    move(n - 1, a, c, b)

    # a에서 c로 이동
    print(a, c)

    # n - 1개의 원반을 기둥 b(보조 기둥 2)에서, a(시작 기둥 1)를 사용하여, c(목표 기둥 3)로 이동
    move(n - 1, b, a, c)

  n = int(input())

  # 옮긴 횟수 k는 원판의 개수 n에 의해 정해짐
  k = 2 ** n - 1
  print(k)

  # n개의 원반을 시작 기둥 1에서, 보조 기둥 2를 사용하여 목표 기둥 3으로 이동
  move(n, 1, 2, 3)
