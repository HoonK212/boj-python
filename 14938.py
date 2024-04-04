import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import heapq
if __name__ == '__main__':

  def dijkstra():
    dist = [float('inf')] * (r + 2)
    dist[1] = 0
    q = [(0, 1)]
    while q:
      d, v = heapq.heappop(q)
      if dist[v] < d:
        continue
      for w, l in graph[v]:
        if dist[w] > dist[v] + l:
          dist[w] = dist[v] + l
          heapq.heappush(q, (dist[w], w))
    return sum(t if dist[i] <= m else 0 for i, t in enumerate(t_list))


  n, m, r = map(int, input().split())
  t_list =  list(map(int, input().split()))

  graph = [[] for i in range(n + 1)]
  for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))