import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def spread_dust(board):
    for i in range(r):
      for j in range(c):
        if board[i][j] > 0:
          spread = board[i][j] // 5
          for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != -1:
              board[i][j] -= spread
              board[ni][nj] += spread
              print(board)

  def run_air_purifier(board):
    for i in range(r):
      if board[i][0] == -1:
        up = i
        down = i + 1
        break

  def clean(board):
    spread_dust(board)
    run_air_purifier(board)


  r, c, t = map(int, input().split())
  room = [list(map(int, input().split())) for _ in range(r)]

  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  for _ in range(t):
    clean(room)

  ans = 2
  for i in range(r):
    ans += sum(room[i])

  print(ans)