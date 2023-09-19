import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(n, d):
    visited[n] = True
    depth[n] = d

    # 우선, parent[node][0]만 초기화
    #   -> 특정 노드의 1단계 위의 부모 노드 set
    for node in graph[n]:
      if visited[node]:
        continue
      parent[node][0] = n
      dfs(node, d + 1)

  def set_parent():
    dfs(1, 0)

    # parent[node][0]의 정보를 바탕으로, 특정 노드의 (2 ** i)단계 위의 부모 노드 set
    #   -> (2 ** i)단계 위의 부모 노드를 추적하는 것이 LCA2 알고리즘의 핵심 !!!
    for i in range(1, length):
      for j in range(1, n + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]


  def lca(a, b):
    if depth[a] > depth[b]:
      a, b = b, a # a 보다 b의 깊이가 깊도록 치환

    # a와 b의 깊이 동일하게 맞추기
    for i in range(length - 1, -1, -1):
      if depth[b] - depth[a] >= (1 << i): # (2 ** i)를 비트 연산자로 표현
        b = parent[b][i]

    # a와 b의 깊이를 맞춘 후, 동일한 노드라면 해당 노드 반환
    if a == b:
      return a

    # (2 ** i)단계 위의 부모 노드를 추적하며 공통 조상 찾기
    for i in range(length - 1, -1, -1):
      if parent[a][i] != parent[b][i]: # 공통 조상에서부터 갈라지는 지점을 지나쳤기 때문에, a와 b의 위치를 끌어 올려서 다시 추적
        a = parent[a][i]
        b = parent[b][i]

    # 반복문 종료 후 a는 공통 조상의 자식 노드이기 때문에, parent[a][0]를 반환
    return parent[a][0]

  n = int(input())

  # 2 ** 17 = 131072
  # 131072 > 100000
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
