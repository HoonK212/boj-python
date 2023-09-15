import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(n, d):
    visited[n] = True
    depth[n] = d

    for node in graph[n]:
      if visited[node]:
        continue
      parent[node][0] = n
      dfs(node, d + 1)

  def set_parent():
    dfs(1, 0)

    for i in range(1, length):
      for j in range(1, n + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

  def lca(a, b):
    if depth[a] > depth[b]:
      a, b = b, a

    for i in range(length - 1, -1, -1):
      if depth[b] - depth[a] >= (1 << i):
        b = parent[b][i]

    if a == b:
      return a

    for i in range(length - 1, -1, -1):
      if parent[a][i] != parent[b][i]:
        a = parent[a][i]
        b = parent[b][i]

    return parent[a][0]

  n = int(input())
  length = 17
  parent = [[0] * length for _ in range(n + 1)]
  visited = [False] * (n + 1)
  depth = [0] * (n + 1)

  graph = [[] for _ in range(n + 1)]
  for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  set_parent()

  m = int(input())
  for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
