import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import copy
from itertools import combinations
if __name__ == '__main__':

  def solution():
    global answer

    for c in combinations(empty, wall):
      coord_new = copy.deepcopy(coordinates)
      for x, y in c:
        coord_new[x][y] = 1

      virus = [(i, j) for i in range(n) for j in range(m) if coord_new[i][j] == 2]
      while virus:
        x, y = virus.pop()
        for dx, dy in direction:
          nx = x + dx
          ny = y + dy
          if 0 <= nx < n and 0 <= ny < m and coord_new[nx][ny] == 0:
            coord_new[nx][ny] = 2
            virus.append((nx, ny))

      safe_zone = 0
      for c in coord_new:
        safe_zone += c.count(0)
      answer = max(answer, safe_zone)


  if __name__ == "__main__":
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    wall = 3

    n, m = map(int, input().split())
    coordinates = [list(map(int, input().split())) for _ in range(n)]
    empty = [(i, j) for i in range(n) for j in range(m) if coordinates[i][j] == 0]

    answer = 0
    solution()
    print(answer)
