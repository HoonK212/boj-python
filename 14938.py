import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import heapq
if __name__ == '__main__':

  def dijkstra(start):
    distances = [inf] * (n + 1)
    queue = []

    # 시작 지역에 대한 거리를 0으로 설정하고, 큐에 삽입
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
      # 가장 짧은 거리의 지역 정보를 큐에서 꺼내기
      current_distance, current_location = heapq.heappop(queue)

      # 이미 처리된 지역이면 무시
      if distances[current_location] < current_distance:
        continue

      # 현재 지역과 인접한 지역들을 확인
      for adj in graph[current_location]:
        adj_location, adj_distance = adj
        cost = current_distance + adj_distance

        # 현재 지역을 거쳐서 인접 지역으로 이동하는 거리가 더 짧을 경우
        if cost < distances[adj_location]:
          distances[adj_location] = cost
          heapq.heappush(queue, (cost, adj_location))

    return distances


  n, m, r = map(int, input().split())
  items = [0] + list(map(int, input().split()))

  graph = [[] for _ in range(n + 1)]
  for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

  inf = int(1e9)

  max_items = 0

  # 모든 지역에 대해 다익스트라 알고리즘 수행
  for i in range(1, n + 1):
    collected_items = 0
    distances = dijkstra(i)

    # 수색 범위 m 이내에 존재하는 아이템 모두 수집
    for j in range(1, n + 1):
      if distances[j] <= m:
        collected_items += items[j]

    # 최대 아이템 개수 갱신
    max_items = max(max_items, collected_items)

  print(max_items)