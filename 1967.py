import sys; input = sys.stdin.readline;
import heapq
if __name__ == '__main__':

  def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
      cost, way = heapq.heappop(queue)
      if cost > distance[way]:
        continue
      last_cost = cost
      last_way = way
      for new_cost, new_way in graph[way]:
        if cost + new_cost < distance[new_way]:
          distance[new_way] = cost + new_cost
          heapq.heappush(queue, (distance[new_way], new_way))

    return last_cost, last_way

  n = int(input())
  graph = [[] for _ in range(n + 1)]

  for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

  INF = int(1e9)

  temp_cost, temp_way = dijkstra(1)
  result_cost, result_way = dijkstra(temp_way)

  print(result_cost)
