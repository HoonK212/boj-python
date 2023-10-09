import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  total = 1 # 방이 총 몇 개인지?
  layer = 1 # 벌집 구조가 몇 겹인지?

  while total < n:
    total += layer * 6 # (layer * 6)만큼 증가하는 것이 핵심 !!!
    layer += 1

  print(layer)
