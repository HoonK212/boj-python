import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from collections import deque
if __name__ == '__main__':

  t = int(input())

  for _ in range(t):
    p = input()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')

    if n == 0:
      queue = []
    else:
      queue = deque(arr)

    flag = 0
    for i in p:
      if i == 'R':
        flag += 1
      elif i == 'D':
        if len(queue) == 0:
          print("error")
          break
        else:
          if flag % 2 == 0:
            queue.popleft()
          else:
            queue.pop()
      else:
        if flag % 2 == 0:
          print("[" + ",".join(queue) + "]")
        else:
          queue.reverse()
          print("[" + ",".join(queue) + "]")
