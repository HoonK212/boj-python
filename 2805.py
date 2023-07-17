import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n, m = map(int, input().split())
  tree_list = list(map(int, input().split()))
  start, end = 0, max(tree_list)

  answer = 0
  while start <= end:
    mid = (start + end) // 2

    total = 0
    for tree in tree_list:
      if tree > mid:
        total += tree - mid

    if total < m:
      end = mid - 1
    else:
      start = mid + 1
      answer = mid

  print(answer)
