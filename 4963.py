import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(y, x):
    if x < 0 or x >= w or y < 0 or y >= h: # 범위를 멋어날 경우, 재귀 종료
      return False

    if coordinates[y][x] == 1: # 현재 좌표가 땅(1)인 경우, 해당 땅을 방문 처리 (0으로 변경)
      coordinates[y][x] = 0

      # 상하좌우로 인접한 땅 탐색
      dfs(y - 1, x)
      dfs(y + 1, x)
      dfs(y, x - 1)
      dfs(y, x + 1)

      # 대각선으로 인접한 땅 탐색
      dfs(y - 1, x - 1)
      dfs(y - 1, x + 1)
      dfs(y + 1, x - 1)
      dfs(y + 1, x + 1)
      return True
    return False


  while True:
    w, h = map(int, input().split())

    if w == 0 & h == 0:
      break

    coordinates = []
    for _ in range(h):
      coordinates.append(list(map(int, input().split())))

    answer = 0 # 섬의 개수
    for i in range(h):
      for j in range(w):
        if dfs(i, j):
          answer += 1

    print(answer)