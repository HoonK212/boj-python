import sys; input = sys.stdin.readline;
from heapq import heappush, heappop
if __name__ == '__main__':

  def dijkstra(start):
    total_cost = [INF] * (n + 1)
    total_cost[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
      # 'heappop'을 사용하기 때문에, 가장 cost가 작은 cost&way 쌍을 pop
      cost, way = heappop(queue)
      if cost > total_cost[way]:
        continue
      last_cost = cost
      last_way = way
      for new_cost, new_way in graph[way]:
        # 새로 계산한 cost가 int(1e9)보다 작으면, 다시 말해 한번도 계산한 적이 없으면 if문 내부 로직 수행
        if cost + new_cost < total_cost[new_way]:
          total_cost[new_way] = cost + new_cost
          heappush(queue, (total_cost[new_way], new_way))

    return last_cost, last_way

  n = int(input())
  graph = [[] for _ in range(n + 1)]

  for _ in range(n - 1):
    a, b, c = map(int, input().split())
    # 'a'에서 cost 'c'를 지불하여 'b'로 이동하는 way 정보 저장 ('a'와 'b'를 치환해, 양방향으로 저장)
    graph[a].append((c, b))
    graph[b].append((c, a))

  INF = int(1e9)

  # 1에서 출발해, 가장 cost가 높은 temp_way 도출
  temp_cost, temp_way = dijkstra(1)

  # temp_way에서 출발해, 가장 cost가 높은 result_way 도출
  result_cost, result_way = dijkstra(temp_way)

  # 주어진 graph 내에서 가장 cost가 높은 temp_way와 result_way를 잇는, result_cost 출력
  print(result_cost)
