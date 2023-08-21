import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  nums = list(map(int, input().split())) # '현재 줄 서있는 곳'
  stack = [0] # '한 명씩만 설 수 있는 공간'

  idx = 1
  for num in nums:
    # '현재 줄 서있는 곳'에서 자기 차례인 경우 간식 수령
    if num == idx:
      idx = idx + 1
      continue

    # '한 명씩만 설 수 있는 공간'에서 자기 차례인 학우들 모두 순차적(선입후출)으로 간식 수령
    while True:
      if stack[-1] == idx:
        stack.pop()
        idx = idx + 1
      else:
        break

    # '현재 줄 서있는 곳'에서 '한 명씩만 설 수 있는 공간'으로 이동
    stack.append(num)
    continue

  # '현재 줄 서있는 곳'이 빈 후, '한 명씩만 설 수 있는 공간'의 학우들 간식 수령
  for _ in range(n - idx + 1):
    if stack[-1] == idx:
      stack.pop()
      idx = idx + 1
      continue
    else:
      print("Sad")
      exit()

  print("Nice")
