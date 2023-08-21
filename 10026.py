import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  def solution(char, answer):
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
      for y in range(n):
        if visited[x][y] is False:
          visited[x][y] = True
          # 신규 구역 발견
          if graph[x][y] == char:
            answer[char] = answer[char] + 1
            # 발견한 구역의 경계 확인
            bfs(char, visited, (x, y))

  def bfs(char, visited, coordinates):
    queue = deque()
    queue.append(coordinates)

    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
          visited[nx][ny] = True
          if graph[nx][ny] == char:
            queue.append((nx, ny))

  n = int(input())
  graph = [str(input().rstrip()) for _ in range(n)]

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  answer1 = {'R': 0, 'G': 0, 'B': 0}
  answer2 = {'R': 0, 'B': 0}

  # 적록색약이 아닌 경우
  for char in answer1.keys():
    solution(char, answer1)

  # 적록색약 적용
  for i in range(n):
    graph[i] = graph[i].replace('G', 'R')

  # 적록색약인 경우
  solution('R', answer2)
  answer2['B'] = answer1['B']

  print(sum(answer1.values()), sum(answer2.values()))
