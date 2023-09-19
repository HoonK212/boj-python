import sys; input = sys.stdin.readline
from collections import Counter
if __name__ == '__main__':

  dice = list(map(int, input().split()))
  dice.sort(reverse=True)
  dice_most = Counter(dice).most_common(1)[0]

  # dice_most[0]: 가장 많이 중복된 주사위 눈 중, 가장 큰 수
  # dice_most[1]: 위 주사위 눈의 중복 횟수
  if dice_most[1] == 1:
    print(dice_most[0] * 100)
  elif dice_most[1] == 2:
    print(dice_most[0] * 100 + 1000)
  else:
    print(dice_most[0] * 1000 + 10000)
