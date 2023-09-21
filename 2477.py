import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  k = int(input())

  # rotate 함수를 사용하기 위해, deque로 선언
  directions = deque()
  lengths = deque()

  for _ in range(6):
    direction, length = map(int, input().split())
    directions.append(direction)
    lengths.append(length)

  # 면적 계산의 편이성을 위해, 예를 들어 423131과 같은 형태로 정렬될 때까지 rotate 실행
  #   -> 일정하게 반시계방향으로 정보가 주어지기 때문에 rotate를 반복해도 밭의 모양은 불변
  while True:
    if directions[2] == directions[4] and directions[3] == directions[5]:
      break
    else:
      directions.rotate(-1)
      lengths.rotate(-1)

  big_square = lengths[0] * lengths[1]
  small_square = lengths[3] * lengths[4]
  print(k * (big_square - small_square))
