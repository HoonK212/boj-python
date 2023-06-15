import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from bisect import bisect_left, bisect_right
if __name__ == '__main__':

  n = int(input())
  first_card_list = list(map(int, input().split()))
  first_card_list.sort()

  m = int(input())
  second_card_list = list(map(int, input().split()))

  # 같은 숫자가 존재하는 경우에만 bisect_left와 bisect_right의 index 값이 달라진다는 것이 핵심 !!!
  for card in second_card_list:
    l = bisect_left(first_card_list, card)
    r = bisect_right(first_card_list, card)
    print(r - l, end=' ')
