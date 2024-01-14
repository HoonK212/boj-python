import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n = int(input())
  xy_li = [list(map(int, input().split())) for _ in range(n)]

  sort_xy = sorted(xy_li, key=lambda x: x[0])
  min = sort_xy[0][0]
  reverse_xy = sorted(xy_li, key=lambda x: x[1], reverse=True)
  max = reverse_xy[0][1]

  arr = [0] * (max - min)

  for xy in sort_xy:
    arr[xy[0] - min] = 1
    arr[xy[1] - min - 1] = 1

  print(sum(arr))
