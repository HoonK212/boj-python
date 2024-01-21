import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from itertools import combinations_with_replacement
if __name__ == '__main__':

  numbers = [1, 5, 10, 50]
  n = int(input())
  result = []

  for cwr in combinations_with_replacement(range(4), n):
    sum = 0
    for i in cwr:
      sum += numbers[i]
    result.append(sum)

  print(len(set(result)))
