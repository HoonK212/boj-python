import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  def left_rotate(num, d):
    # num 범위 체크 및 2번칸과 6번칸 비교
    if num < 1 or gears[num][2] == gears[num + 1][6]:
      return
    # 2번칸과 6번칸이 같지 않으면, 재귀 호출 및 rotate 실행
    if gears[num][2] != gears[num + 1][6]:
      left_rotate(num - 1, -d)
      gears[num].rotate(d)

  def right_rotate(num, d):
    if num > 4 or gears[num - 1][2] == gears[num][6]:
      return
    if gears[num - 1][2] != gears[num][6]:
      right_rotate(num + 1, -d)
      gears[num].rotate(d)

  gears = [[]]
  for _ in range(4):
    gears.append(deque(list(map(int, list(input().rstrip()))))) # rotate(direction) 함수를 사용하기 위해, deque로 append 하는 것이 핵심 !!!

  n = int(input())
  for _ in range(n):
    num, d = map(int, input().split())

    # 좌, 우 톱니들 먼저 rotate 실행
    left_rotate(num - 1, -d)
    right_rotate(num + 1, -d)

    # num 톱니 rotate 실행
    gears[num].rotate(d)

  answer = 0
  for i in range(4):
    answer += (2 ** i) * gears[i + 1][0]
  print(answer)
