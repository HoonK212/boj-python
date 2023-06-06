
import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import math
if __name__ == '__main__':

  t = int(input())
  for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if r1 == r2 and distance == 0:
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2) :
        print(2)
    else:
        print(0)
