import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n, k = map(int, input().split())
  coin_list = [int(input()) for _ in range(n)]

  answer = 0
  for coin in reversed(coin_list):
    if coin > k:
      continue

    cnt = k // coin
    k = k - (coin * cnt)
    answer += cnt

  print(answer)
