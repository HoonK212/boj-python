import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  memo = str(input()).rstrip()

  # 메모의 길이가 0보다 크고 50보다 작기 때문에, 미로의 최대 크기는 101 * 101로 설정하는 것이 핵심 !!!
  maze = [['#'] * 101 for _ in range(101)]

  # 방향 설정 (남쪽부터 시계방향 순서)
  direction = 0
  di = [1, 0, -1, 0]
  dj = [0, -1, 0, 1]

  # 시작 좌표 설정
  i, j = 50, 50
  maze[i][j] = '.'

  # 미로의 실제 크기를 측정하기 위한 변수 초기화
  min_i, min_j = 50, 50
  max_i, max_j = 50, 50

  for move in memo:
    # 방향 전환
    if move == 'L':
      direction += 3
    elif move == 'R':
      direction += 1
    else:
      # 좌표 이동
      i += di[direction % 4]
      j += dj[direction % 4]
      maze[i][j] = '.'

      # 미로의 실제 크기를 측정하기 위해 최소, 최대 비교
      min_i = min(min_i, i)
      min_j = min(min_j, j)
      max_i = max(max_i, i)
      max_j = max(max_j, j)

  # 범위를 실제 크기로 제한하여 미로 지도 출력
  for i in range(min_i, max_i + 1):
    print(*maze[i][min_j : max_j + 1], sep="")
