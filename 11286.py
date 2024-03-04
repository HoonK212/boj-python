import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import heapq
if __name__ == '__main__':

  n = int(input())
  heap = []

  for _ in range(n):
    x = int(input())

    if x:
      heapq.heappush(heap, (abs(x), x))
    else:
      try:
        print(heapq.heappop(heap)[1])
      except:
        print(0)