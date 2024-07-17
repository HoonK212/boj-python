import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import deque
if __name__ == '__main__':

  def solve():
    # 정점(v)과 간선(e)의 수 입력 받기
    v, e = map(int, input().split())

    # 그래프를 표현하기 위한 변수들 초기화
    # 각 정점에 대해 'in' 노드와 'out' 노드를 추가로 생성하므로 길이는 2 * v + 1
    length = v * 2 + 1

    # flow: 유량을 저장하는 배열
    # capacity: 용량을 저장하는 배열
    # cost: 비용을 저장하는 배열
    # connect: 연결된 정점 정보를 저장하는 배열
    flow = [[0] * length for _ in range(length)]
    capacity = [[0] * length for _ in range(length)]
    cost = [[0] * length for _ in range(length)]
    connect = [[] for _ in range(length)]

    # 각 정점에 대해 'in' 노드와 'out' 노드를 연결
    for i in range(1, v + 1):
      connect[i].append(i + v)
      connect[i + v].append(i)
      capacity[i][i + v] = 1  # 'in' 노드와 'out' 노드의 용량을 1로 설정

    # 간선 정보 입력받기 및 그래프 구성
    for _ in range(e):
      a, b, c = map(int, input().split())
      connect[a + v].append(b)
      connect[b].append(a + v)
      capacity[a + v][b] = 1
      cost[a + v][b] = c
      cost[b][a + v] = -c

    # 시작점과 끝점 설정
    start = 1 + v
    end = v
    total_cost = 0

    # 두 개의 독립적인 경로를 찾기 위해 SPFA 알고리즘을 두 번 실행
    for _ in range(2):
      # SPFA 알고리즘 초기화
      prev = [-1] * length
      distance = [float('inf')] * length
      in_queue = [False] * length
      queue = deque([start])
      distance[start] = 0
      in_queue[start] = True

      # SPFA 알고리즘 실행
      while queue:
        u = queue.popleft()
        in_queue[u] = False
        for v in connect[u]:
          if capacity[u][v] - flow[u][v] > 0 and distance[v] > distance[u] + cost[u][v]:
            distance[v] = distance[u] + cost[u][v]
            prev[v] = u
            if not in_queue[v]:
              queue.append(v)
              in_queue[v] = True

      # 유량 조정 및 비용 계산
      u = end
      while u != start:
        flow[prev[u]][u] += 1
        flow[u][prev[u]] -= 1
        total_cost += cost[prev[u]][u]
        u = prev[u]

    # 최소 비용 출력
    print(total_cost)

  # EOF까지 여러 테스트 케이스 처리
  while True:
    try:
      solve()
    except:
      break