import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  def dfs(start, end):

    queue = deque()
    queue.append(node_links[start])
    answer = 1
    visited_nodes = [False for _ in range(n + 1)]
    visited_nodes[start] = True

    while queue:
      node_link = queue.pop()

      if end in node_link:
        return answer

      for node in node_link:
        if not visited_nodes[node]:
          queue.append(node_links[node])
          visited_nodes[node] = True
        answer = answer + 1
        break

      if not queue:
        return -1

  n = int(input())
  node_links = [[] for _ in range(n + 1)]

  start_node, end_node = map(int, input().split())

  m = int(input())
  for _ in range(m):
    node1, node2 = map(int, input().split())
    node_links[node1].append(node2)
    node_links[node2].append(node1)

  print(dfs(start_node, end_node))

# 10
# 7 10
# 8
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
# 9 10