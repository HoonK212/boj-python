import sys; input = sys.stdin.readline
if __name__ == '__main__':

  def move_right():
    tmp = dice[1]
    dice[1] = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = tmp

  def move_left():
    tmp = dice[4]
    dice[4] = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = tmp

  def move_back():
    tmp = dice[5]
    dice[5] = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = tmp

  def move_front():
    tmp = dice[3]
    dice[3] = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = tmp

  n, m, x, y, k = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(n)]
  command = list(map(int, input().split()))

  # [밑면, 좌, 앞, 뒤, 우, 윗면]
  dice = [0, 0, 0, 0, 0, 0]

  # [동, 서, 북, 남]
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]

  for i in command:
    if 0 <= x + dx[i - 1] < n and 0 <= y + dy[i - 1] < m:
      x, y = x + dx[i - 1], y + dy[i - 1]

      if i == 1:
        move_right()
      elif i == 2:
        move_left()
      elif i == 3:
        move_back()
      elif i == 4:
        move_front()

      if graph[x][y] == 0:
        graph[x][y] = dice[0]
      else:
        dice[0] = graph[x][y]
        graph[x][y] = 0

      print(dice[5])
