import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  def fishing():
    global answer

    for i in range(C):
      for j in range(R):
        if graph[j][i]: # 해당 위치에 상어 존재
          answer += graph[j][i][0][2] # 상어의 크기 합산
          graph[j][i].remove(graph[j][i][0])
          break

      move()

      for k in range(R):
        for l in range(C):
          if 1 < len(graph[k][l]): # 한 위치에 여러 마리의 상어가 존재
            # 상어의 크기 역순으로 pop()
            graph[k][l].sort(key=lambda x: x[2], reverse=True)
            while 1 < len(graph[k][l]):
              graph[k][l].pop()


  def move():
    tmp_graph = [[[] for _ in range(C)] for _ in range(R)]

    for i in range(R):
      for j in range(C):
        if graph[i][j]:

          x, y = i, j
          s, d, z = graph[i][j][0]
          distance = s

          while 0 < distance:
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if 0 <= nx < R and 0 <= ny < C: # 격자판 내에서 방향에 맞게 이동
              x, y = nx, ny
              distance -= 1
            else: # 격자판의 경계를 넘는 경우, 방향을 전환해서 이동
              if d == 0 or d == 2:
                d += 1
              elif d == 1 or d == 3:
                d -= 1
          tmp_graph[x][y].append([s, d, z])

    # tmp_graph로 graph 초기화
    for i in range(R):
      for j in range(C):
        graph[i][j] = tmp_graph[i][j]


  R, C, M = map(int, input().split())
  direction = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 이동 방향 설정
  graph = [[[] for _ in range(C)] for _ in range(R)]
  for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r - 1][c - 1].append([s, d - 1, z]) # 한 위치에 여러 마리의 상어가 겹칠 수도 있도록, append()로 처리

  answer = 0
  fishing()
  print(answer)
