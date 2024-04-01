import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def spread_dust(r, c, room): # 미세먼지를 확산시키는 함수
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tmp_board = [[0] * c for _ in range(r)]  # 확산된 미세먼지를 임시로 저장할 공간

    for i in range(r):
      for j in range(c):
        if room[i][j] > 0:
          spread_amt = room[i][j] // 5
          spread_cnt = 0

          for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
              tmp_board[ni][nj] += spread_amt
              spread_cnt += 1

          room[i][j] -= spread_amt * spread_cnt

    for i in range(r):
      for j in range(c):
        room[i][j] += tmp_board[i][j]


  def run_air_purifier(r, c, room, purifier): # 공기청정기 작동 함수
    upper, lower = purifier

    # 위쪽 공기청정기 반시계방향 순환
    for i in range(upper - 1, 0, -1):
      room[i][0] = room[i - 1][0]
    for i in range(c - 1):
      room[0][i] = room[0][i + 1]
    for i in range(upper):
      room[i][c - 1] = room[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
      room[upper][i] = room[upper][i - 1]
    room[upper][1] = 0 # 공기청정기 바로 옆 칸은 미세먼지 X

    # 아래쪽 공기청정기 시계방향 순환
    for i in range(lower + 1, r - 1):
      room[i][0] = room[i + 1][0]
    for i in range(c - 1):
      room[r - 1][i] = room[r - 1][i + 1]
    for i in range(r - 2, lower - 1, -1):
      room[i + 1][c - 1] = room[i][c - 1]
    for i in range(c - 1, 1, -1):
      room[lower][i] = room[lower][i - 1]
    room[lower][1] = 0 # 공기청정기 바로 옆 칸은 미세먼지 X


  def find_purifier(r, room): # 공기청정기 위치 찾기
    for i in range(r):
      if room[i][0] == -1:
        return (i, i + 1)


  def simulate(r, c, t, room):
    purifier = find_purifier(r, room)

    for _ in range(t):
      spread_dust(r, c, room)
      run_air_purifier(r, c, room, purifier)

    total_dust = sum(sum(row) for row in room) + 2  # 공기청정기 위치의 값이 -1이므로, 최종 합에 + 2
    return total_dust


  r, c, t = map(int, input().split())
  room = [list(map(int, input().split())) for _ in range(r)]

  print(simulate(r, c, t, room))