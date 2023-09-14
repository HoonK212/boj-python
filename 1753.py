import sys; input = sys.stdin.readline
from heapq import heappush, heappop
if __name__ == '__main__':

  def dijkstra(k):
    dp[k] = 0
    hq = []
    heappush(hq, (0, k))

    while hq:
      weight, now = heappop(hq)

      if dp[now] < weight:
        continue

      for w, v in graph[now]:
        w_sum = weight + w
        if w_sum < dp[v]:
          dp[v] = w_sum
          heappush(hq, (w_sum, v))

  V, E = map(int, input().split())
  K = int(input())

  graph = [[] for _ in range(V + 1)]
  for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

  inf = int(1e9)
  dp = [inf] * (V + 1)

  dijkstra(K)

  for i in range(1, V + 1):
    print("INF" if dp[i] == inf else dp[i])
