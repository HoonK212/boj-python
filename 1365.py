
import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from bisect import bisect_left

if __name__ == '__main__':

  n = int(input())
  line = list(map(int, input().split()))

  dp = [1]
  answer = [line[0]]

  for i in range(n):
    if line[i] > answer[-1]:
      answer.append(line[i])
      dp.append(dp[-1] + 1)
    else:
      idx = bisect_left(answer, line[i])
      answer[idx] = line[i]

  print(n - dp[-1])
