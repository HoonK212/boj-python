import sys; input = sys.stdin.readline
from heapq import heappush, heappop
if __name__ == '__main__':

  def dijkstra(k):
    dp[k] = 0 # dp[k]는 'k 지점에서 k 지점으로 이동하기 위한 가중치'라는 의미이므로 0으로 초기화
    hq = []
    heappush(hq, (0, k))

    while hq:
      weight, now = heappop(hq)

      # 최단 경로를 구하는 중이므로, dp[now]의 가중치 값이 더 작으면 계산할 필요 없음
      if dp[now] < weight:
        continue

      for w, v in graph[now]:
        w_sum = weight + w

        # 가중치를 합한 값이 dp[now]의 가중치 값보다 작을 경우, 합산 값으로 변경
        if w_sum < dp[v]:
          dp[v] = w_sum

          # 다음 경로로의 반복 계산이 가능하도록 hq에 push
          heappush(hq, (w_sum, v))

  V, E = map(int, input().split())
  K = int(input())

  graph = [[] for _ in range(V + 1)]
  for _ in range(E):
    u, v, w = map(int, input().split())
    # graph[u] = (w, v):
    #   출발 지점 u ---(가중치 w)---> 도착 지점 v
    graph[u].append((w, v))

  inf = int(1e9)
  dp = [inf] * (V + 1)

  dijkstra(K)

  for i in range(1, V + 1):
    print("INF" if dp[i] == inf else dp[i])
