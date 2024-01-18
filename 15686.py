import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from itertools import combinations
if __name__ == '__main__':

  n, m = map(int, input().split())
  city = [list(map(int, input().split())) for i in range(n)]
  house = []
  chicken = []

  for r in range(n):
    for c in range(n):
      if city[r][c] == 1:
        house.append([r, c])
      elif city[r][c] == 2:
        chicken.append([r, c])

  answer = float('inf')
  for c in combinations(chicken, m):
    sum_distance = 0
    for h in house:
      distance = float('inf')
      for i in c:
        distance = min(distance, abs(h[0] - i[0]) + abs(h[1] - i[1]))
      sum_distance += distance
    answer = min(answer, sum_distance)

  print(answer)
