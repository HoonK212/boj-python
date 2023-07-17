import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def recursion(i, j, size):

    # size가 3인지 확인 후, 가장 작은 단위의 트리 모양 완성
    if size == 3:
      for di in range(3):
        for dy in range(di + 1):
          stars[i + di][j - dy] = stars[i + di][j + dy] = "*"
      stars[i + 1][j] = " "
      return

    # 입력된 size를 3이 될때까지 2로 나누고,
    #   (i, j), (i + newSize, j - newSize), (i + newSize, j + newSize) 좌표로 재귀 호출하는 것이 핵심 !!!
    newSize = size // 2
    recursion(i, j, newSize)
    recursion(i + newSize, j - newSize, newSize)
    recursion(i + newSize, j + newSize, newSize)

  n = int(input())
  stars = [[" " for _ in range(n * 2)] for _ in range(n)]

  recursion(0, n - 1, n)

  for star in stars:
    print("".join(star))
