import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from heapq import heappush, heappop
if __name__ == '__main__':

  n = int(input())
  locations = []

  for _ in range(n):
    h, o = map(int, input().split())
    start, end = min(h, o), max(h, o)
    locations.append((start, end)) # h와 o가 정렬된 상태가 아니기에 start, end로 변환 후 append
  locations.sort(key=lambda x: (x[1], x[0])) # end를 기준으로 정렬 후, start로 정렬

  d = int(input())

  q = []
  ans = 0

  for location in locations:
    start, end = location
    heappush(q, start) # heapq에 start push
    rail_start = end - d # end를 기준으로, 철로의 시작점 초기화
    while q and q[0] < rail_start:
      heappop(q) # 철로의 시작점보다 start가 작으면 pop
    ans = max(ans, len(q)) # 최대값으로 ans 초기화

  print(ans)