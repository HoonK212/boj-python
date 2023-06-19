import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(x, y, n):
    global answer
    visited = coordinates[x][y]

    for i in range(x, x + n):
      for j in range(y, y + n):
        # 현재 n * n 크기의 종이가 모두 같은 수로 되어 있는지 검증
        if coordinates[i][j] != visited:
          for k in range(3):
            for l in range(3):
              # 모두 같은 수가 아닌 경우, 같은 크기의 종이 9개로 자른 후 각각의 종이를 재검증
              #   9개로 자른 후 재검증을 위한 재귀 함수의 호출 방법을 찾는 것이 핵심 !!!
              dfs(x + k * n // 3, y + l * n // 3, n // 3)
          return

    # -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수 집계
    if visited == -1:
      answer[0] += 1
    elif visited == 0:
      answer[1] += 1
    elif visited == 1:
      answer[2] += 1

  n = int(input())
  coordinates = [list(map(int, input().split())) for _ in range(n)]

  answer = [0, 0, 0]
  dfs(0, 0, n)

  [print(ans) for ans in answer]
