import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import deque
if __name__ == '__main__':

  def bfs(x, y, size):
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)] # 최소 거리

    queue = deque()
    queue.append((x, y))

    visited[x][y] = True
    candidiates = [] # 타겟 물고기 후보 리스트

    while queue:
      new_x, new_y = queue.popleft()

      for i in range(4):
        nx = new_x + dx[i]
        ny = new_y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
          if graph[nx][ny] <= size: # 사이즈가 같은 경우에도 지나갈 수는 있음
            visited[nx][ny] = True
            distance[nx][ny] = distance[new_x][new_y] + 1
            queue.append((nx, ny))
            if graph[nx][ny] != 0 and graph[nx][ny] < size:
              candidiates.append((nx, ny, distance[nx][ny])) # 후보 리스트에 추가

    # 타겟 물고기 후보 리스트를 타겟 지정 규칙에 따라 정렬
    #   먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    #   먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    #     거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    #     거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    return sorted(candidiates, key=lambda x: (-x[2], -x[0], -x[1]))

  n = int(input())
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  # 아기 상어의 위치 좌표와 크기 초기화
  shark_x, shark_y, shark_size = 0, 0, 2
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 9:
        shark_x = i
        shark_y = j
        break

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  answer = 0 # 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지
  cnt = 0 # 먹은 물고기 수

  while True:
    bfs_result = bfs(shark_x, shark_y, shark_size)

    # 더 이상 먹을 수 있는 물고기가 공간에 없는 경우
    if len(bfs_result) == 0:
      break

    nx, ny, dist = bfs_result.pop()
    graph[shark_x][shark_y], graph[nx][ny] = 0, 0 # 아기 상어의 기존 위치와 타겟 물고기의 위치 0으로 초기화
    answer += dist # 타겟 물고기까지의 거리 합산
    shark_x, shark_y = nx, ny # 아기 상어의 위치 좌표 수정

    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
    cnt += 1
    if cnt == shark_size:
      shark_size += 1
      cnt = 0

  print(answer)
