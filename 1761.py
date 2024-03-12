import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(x, depth):
    visited[x] = True  # 현재 노드 방문 처리
    depths[x] = depth  # 현재 노드 깊이 설정
    for y, cost in graph[x]:  # 현재 노드와 연결된 노드들 순회
      if not visited[y]:
        parent[y] = x  # 부모 노드 정보 저장
        distances[y] = distances[x] + cost  # 거리 정보 저장
        sparse_table[y][0] = x  # 부모 노드 정보를 sparse table에 초기화
        dfs(y, depth + 1)  # 재귀적으로 다음 노드 방문


  def build_sparse_table():
    dfs(1, 0)  # 루트 노드부터 시작해 dfs 실행
    for i in range(1, log_n + 1):  # 각 노드에 대해 j의 2^i번째 조상을 설정
      for j in range(1, n + 1):
        sparse_table[j][i] = sparse_table[sparse_table[j][i - 1]][i - 1]


  def lca(a, b):
    # 깊이가 깊은 노드를 b로 설정
    if depths[a] > depths[b]:
      a, b = b, a

    # 두 노드의 깊이를 동일하게 조정
    for i in range(log_n, -1, -1):
      if depths[b] - depths[a] >= (1 << i):
        b = sparse_table[b][i]

    # 두 노드가 같다면 바로 반환
    if a == b:
      return a

    # lca를 찾을 때까지 반복
    for i in range(log_n, -1, -1):
      if sparse_table[a][i] != sparse_table[b][i]:
        a = sparse_table[a][i]
        b = sparse_table[b][i]

    return parent[a]  # lca 반환


  n = int(input())
  graph = [[] for _ in range(n + 1)]
  for _ in range(n - 1):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

  parent = [0] * (n + 1)  # 각 노드의 부모 노드 정보
  depths = [0] * (n + 1)  # 각 노드의 깊이 정보

  visited = [False] * (n + 1)  # 방문 여부 체크 리스트
  distances = [0] * (n + 1)  # 루트 노드부터 각 노드까지의 거리

  log_n = (n - 1).bit_length()   # 트리의 높이에 대한 로그 값 구하기
  sparse_table = [[-1] * (log_n + 1) for _ in range(n + 1)]  # 2^i번째 조상 정보를 저장할 dp 테이블

  build_sparse_table()  # sparse table 구축

  m = int(input())
  for _ in range(m):
    x, y = map(int, input().split())
    lca_node = lca(x, y)
    print(distances[x] + distances[y] - 2 * distances[lca_node])