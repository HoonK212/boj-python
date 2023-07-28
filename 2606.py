import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import deque
if __name__ == '__main__':

  def bfs(virus):
    global node_list, edge_list, visited_list, queue

    for i, edge in enumerate(edge_list):
      if visited_list[i]:
        continue

      if virus in edge:
        visited_list[i] = True

        for node_idx in edge:
          if node_idx != virus and node_list[node_idx] == 0:
            queue.append(node_idx)
          node_list[node_idx] = 1

    while queue:
      bfs(queue.popleft())

  node_cnt = int(input())
  node_list = [0] * (node_cnt + 1)

  edge_cnt = int(input())
  edge_list = [list(map(int, input().split())) for _ in range(edge_cnt)]

  visited_list = [False] * edge_cnt
  queue = deque()

  bfs(1)
  node_list[1] = 0
  print(node_list.count(1))
