import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def watch(x, y, direction_list):
    # 감시의 중복은 의미가 없으므로, set 사용
    watched_set = set()
    for direction in direction_list:
      nx = x
      ny = y
      while True:
        nx += dx[direction]
        ny += dy[direction]
        # 범위를 벗어나거나 벽을 만났을 경우, break
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 6:
          break
        # 그 외, 원래는 사각 지대였던 좌표를 만나면 감시 좌표로 기록
        elif graph[nx][ny] == 0:
          watched_set.add((nx, ny))
    return watched_set

  def dfs(depth, prev_set): # depth의 의미: 주어진 cctv의 총 개수
    if depth == len(watched_coordinates):
      # 더 많은 좌표를 감시한 경우, result_set 갱신
      if len(prev_set) > len(result_set[0]):
        result_set[0] = prev_set
      return
    for cur_set in watched_coordinates[depth]:
      dfs(depth + 1, prev_set | cur_set) # prev_set과 cur_set의 union

  n, m = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(n)]

  # 좌표의 이동 방향
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # cctv의 type에 따른 감시 방향 (좌표로 표헌)
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
      # 입력 상태의 사각 지대 카운트
      if graph[i][j] == 0:
        blind_cnt += 1
      # cctv의 감시 좌표 기록
      elif graph[i][j] != 0 and graph[i][j] != 6:
        watched_coordinates.append(
          [watch(i, j, direction_list) for direction_list in cctv_type[graph[i][j]]]) # cctv의 위치와 감시 방향을 인자로 watch() 호출

  # 가장 많은 좌표를 감시한 경우인 result_set 선언
  result_set = [set()]
  dfs(0, set())
  print(blind_cnt - len(result_set[0]))
