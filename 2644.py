import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  def bfs(start):

    queue = deque([start])
    visited[start] = True

    while queue:
      node = queue.pop()

      for link_node in node_links[node]:
        if not visited[link_node]:
          visited[link_node] = True
          queue.append(link_node)
          answer[link_node] = answer[node] + 1

  n = int(input())
  start_node, end_node = map(int, input().split())
  m = int(input())

  node_links = [[] for _ in range(n + 1)]
  for _ in range(m):
    node1, node2 = map(int, input().split())
    node_links[node1].append(node2)
    node_links[node2].append(node1)

  visited = [False] * (n + 1)
  answer = [0] * (n + 1)

  # start node를 기준으로 다른 모든 node와의 촌수를 계산 후, end node에 해당하는 값을 출력
  bfs(start_node)
  print(-1 if answer[end_node] == 0 else answer[end_node])

# 사촌
# 11
# 10 11
# 9
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
# 7 10
# 9 11

# 무촌
# 11
# 6 10
# 9
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
# 7 10
# 9 11
