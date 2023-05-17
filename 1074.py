import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n, r, c = map(int, input().split())
  cnt = 0

  while n > 1:
    size = 2 ** (n-1)
    if r < size and c < size:
      pass
    elif r < size <= c:
      c -= size
      cnt += size ** 2
    elif r >= size > c:
      r -= size
      cnt += size ** 2 * 2
    elif r >= size and c >= size:
      r -= size
      c -= size
      cnt += size ** 2 * 3
    n -= 1

  if r == 0 and c == 0:
    print(cnt)
  if r == 0 and c == 1:
    print(cnt + 1)
  if r == 1 and c == 0:
    print(cnt + 2)
  if r == 1 and c == 1:
    print(cnt + 3)
