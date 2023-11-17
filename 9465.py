import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  t = int(input())
  for i in range(t):
    arr = []
    n = int(input())

    for i in range(2):
      arr.append(list(map(int, input().split())))

    for i in range(1, n):
      if i == 1:
        arr[0][i] += arr[1][i - 1]
        arr[1][i] += arr[0][i - 1]
      else:
        arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
        arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])

    print(max(arr[0][n - 1], arr[1][n - 1]))
