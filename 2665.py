import sys; input = sys.stdin.readline
from heapq import heappush, heappop
if __name__ == '__main__':

  def dijkstra(s_x, s_y, e_x, e_y):
    visited[s_x][s_y] = True
    hq = []

    # cnt를 기준으로 heapq를 사용하는 것이 핵심 !!!
    heappush(hq, [0, s_x, s_y])

    while hq:
      cnt, x, y = heappop(hq)

      if x == e_x and y == e_y:
        return cnt

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
          visited[nx][ny] = True

          if graph[nx][ny] == 0:
            # 다음 방이 검은 방인 경우에만 cnt++
            heappush(hq, [cnt + 1, nx, ny])
          else:
            heappush(hq, [cnt, nx, ny])

  n = int(input())
  graph = [list(map(int, input().rstrip())) for _ in range(n)]

  visited = [[False] * n for _ in range(n)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  print(dijkstra(0, 0, n - 1, n - 1))
