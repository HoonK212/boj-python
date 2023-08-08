import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def watch(x, y, direction_list):
    watched_coordinate = set()
    for direction in direction_list:
      nx = x
      ny = y
      while True:
        nx += dx[direction]
        ny += dy[direction]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 6:
          break
        elif graph[nx][ny] == 0:
          watched_coordinate.add((nx, ny))
    return watched_coordinate

  def dfs(depth, prev_set):
    if depth == len(watched_coordinates):
      if len(prev_set) > len(watched_set[0]):
        watched_set[0] = prev_set
      return
    for cur_set in watched_coordinates[depth]:
      dfs(depth + 1, prev_set | cur_set)

  n, m = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(n)]

  dx= [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  cctv_type = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
  }

  blind_cnt = 0
  watched_coordinates = []

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        blind_cnt += 1
      elif graph[i][j] != 0 and graph[i][j] != 6:
        watched_coordinates.append(
          [watch(i, j, direction_list) for direction_list in cctv_type[graph[i][j]]])

  watched_set = [set()]

  dfs(0, set())
  print(blind_cnt - len(watched_set[0]))
