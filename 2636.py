import sys; input = sys.stdin.readline;
from collections import deque
if __name__ == '__main__':

  def bfs():
    queue = deque()
    queue.append([0, 0])

    # bfs function이 호출될 때마다 초기화 된 visited 필요
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    cnt = 0
    while queue:
      x, y = queue.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:

          if coordinates[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append([nx, ny])

          # coordinates[nx][ny] == 1일 때는 queue에 추가하지 않는 것이 핵심 !!!
          elif coordinates[nx][ny] == 1:
            visited[nx][ny] = 1
            coordinates[nx][ny] = 0 # 치즈가 녹는 로직
            cnt += 1 # 녹은 치즈 counting

    answer.append(cnt)
    return cnt

  n, m = map(int, input().split())
  coordinates = []
  for i in range(n):
    coordinates.append(list(map(int, input().split())))

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  time = 0
  answer = []

  # 시간(time)을 측정하며, 치즈를 녹이는 bfs function 반복
  while 1:
    time += 1

    # bfs function의 return이 0이면 더 이상 남은 치즈가 없으므로 반복문 종료
    if bfs() == 0:
      break

  # 'time += 1' 연산 후 bfs function을 호출하기 때문에, time -1 출력
  print(time - 1)

  # 마지막 cnt는 0이므로, 모두 녹기 한 시간 전에 남아있는 치즈조각의 수로 answer[-2] 출력
  print(answer[-2])
