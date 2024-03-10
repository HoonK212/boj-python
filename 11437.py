import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(node, d, par):
    # 노드의 부모와 깊이 저장
    parent[node] = par
    depth[node] = d
    # 해당 노드의 자식들에 대해서 재귀적으로 dfs 수행
    for child in tree[node]:
      if child != par:
        dfs(child, d + 1, node)


  def build_sparse_table(n):
    # 초기 sparse table 구성
    for i in range(1, n + 1):
      sparse_table[i][0] = parent[i]

    # sparse table 채우기
    for j in range(1, log_n + 1):
      for i in range(1, n + 1):
        if sparse_table[i][j - 1] != -1:
          sparse_table[i][j] = sparse_table[sparse_table[i][j - 1]][j - 1]


  def lca(a, b):
    if depth[a] < depth[b]:
      a, b = b, a

    # 두 노드의 깊이 맞추기
    for i in range(log_n, -1, -1):
      if depth[a] - (1 << i) >= depth[b]:
        a = sparse_table[a][i]

    if a == b:
      return a

    # 두 노드를 동시에 올려 부모가 같아질 때까지 반복
    for i in range(log_n, -1, -1):
      if sparse_table[a][i] != -1 and sparse_table[a][i] != sparse_table[b][i]:
        a = sparse_table[a][i]
        b = sparse_table[b][i]

    return parent[a]


  n = int(input())
  tree = [[] for _ in range(n + 1)]
  for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

  # 트리의 높이에 대한 로그 값 구하기
  log_n = (n - 1).bit_length()
  # 각 노드의 부모, 깊이, sparse table 초기화
  parent = [-1] * (n + 1)
  depth = [0] * (n + 1)
  sparse_table = [[-1] * (log_n + 1) for _ in range(n + 1)]

  # dfs를 통해 각 노드의 부모와 깊이 구하기
  dfs(1, 0, -1)
  # sparse table 구축
  build_sparse_table(n)

  m = int(input())
  for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))