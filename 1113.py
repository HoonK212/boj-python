import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import deque
if __name__ == '__main__':

  def bfs(i, j):
    global answer
    visited = [[False] * m for _ in range(n)] # 방문 여부 체크
    visited[i][j] = True  # 시작 위치 방문 체크

    height = pool[i][j]  # 현재 위치의 높이
    min_height = 9  # 현재 탐색 영역에서의 최소 벽 높이 (초기값은 최대 높이인 9로 설정)

    queue = deque([(i, j)])  # bfs를 위한 큐, 시작 위치 추가
    mini_pool = [(i, j)]  # 현재 탐색 중인 영역의 좌표들

    while queue:
      x, y = queue.popleft()  # 큐에서 현 위치 꺼내기

      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 범위를 벗어나면 외부와 접해 있는 것이므로 물을 채울 수 없음
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return 0, 0

        # 현재 높이보다 낮거나 같은 곳으로만 이동 가능
        if not visited[nx][ny] and pool[nx][ny] <= height:
          visited[nx][ny] = True
          queue.append((nx, ny))
          mini_pool.append((nx, ny))
        # 벽을 만났을 때 최소 높이 갱신
        elif pool[nx][ny] > height:
          min_height = min(min_height, pool[nx][ny])

    # 물을 채울 수 있는 높이 계산
    water_volume = 0
    for x, y in mini_pool:
      water_volume += (min_height - pool[x][y])
      pool[x][y] = min_height  # 물을 채운 후 높이 갱신

    return water_volume, len(mini_pool)

  n, m = map(int, input().split())
  pool = [list(map(int, input().strip())) for _ in range(n)]

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  answer = 0

  # 테두리는 제외하고 탐색
  for i in range(1, n - 1):
    for j in range(1, m - 1):
      if pool[i][j] != 9:  # 9는 최대 높이이기 때문에, 물을 채울 수 없음
        volume, cells = bfs(i, j)
        answer += volume

  print(answer)