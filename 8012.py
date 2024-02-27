import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import defaultdict
if __name__ == '__main__':

  def dfs(tree, node, depth, parent):
    for next_node in tree[node]:
      if depth[next_node] == -1:  # 아직 방문하지 않은 노드인 경우
        parent[next_node] = node
        depth[next_node] = depth[node] + 1
        dfs(tree, next_node, depth, parent)


  def lca(a, b, depth, parent):
    # depth가 동일하도록 조정
    while depth[a] != depth[b]:
      if depth[a] > depth[b]:
        a = parent[a]
      else:
        b = parent[b]

    # lca를 찾을 때까지 재탐색
    while a != b:
      a = parent[a]
      b = parent[b]

    return a


  def min_travel_time_lca(n, roads, m, cities):
    tree = defaultdict(list)
    for a, b in roads:
      tree[a].append(b)
      tree[b].append(a)

    # 깊이, 부모 초기화
    depth = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    depth[1] = 0  # 포항의 depth는 0

    # dfs를 사용하여 깊이와 부모 노드 계산
    dfs(tree, 1, depth, parent)

    # 방문 도시 순서에 따라 최소 이동 시간 계산
    total_time = 0
    for i in range(m - 1):
      # 현재 도시와 다음 도시의 lca 찾기
      lca_node = lca(cities[i], cities[i + 1], depth, parent)

      # 포항에서 현재 도시와 다음 도시까지의 거리, 두 도시 사이 거리 계산
      distance = depth[cities[i]] + depth[cities[i + 1]] - 2 * depth[lca_node]
      total_time += distance

    return total_time


  n = int(input())
  roads = []
  for _ in range(n - 1):
    a, b = map(int, input().split())
    roads.append((a, b))

  m = int(input())
  cities = []
  for _ in range(m):
    city = int(input())
    cities.append(city)

  # 최소 시간 계산
  min_time_lca = min_travel_time_lca(n, roads, m, cities)
  print(min_time_lca)