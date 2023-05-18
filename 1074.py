import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n, r, c = map(int, input().split())
  cnt = 0

  while n > 1:
    size = 2 ** (n-1)
    if r < size and c < size: # 좌상단
      pass
    elif r < size <= c: # 우상단
      c -= size
      cnt += size ** 2
    elif r >= size > c: # 좌하단
      r -= size
      cnt += size ** 2 * 2
    elif r >= size and c >= size: # 우하단
      r -= size
      c -= size
      cnt += size ** 2 * 3
    n -= 1

  if r == 0 and c == 0: # 좌상단
    print(cnt)
  if r == 0 and c == 1: # 우상단
    print(cnt + 1)
  if r == 1 and c == 0: # 좌하단
    print(cnt + 2)
  if r == 1 and c == 1: # 우하단
    print(cnt + 3)
