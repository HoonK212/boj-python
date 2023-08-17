import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  nums = list(map(int, input().split()))
  stack = [0]

  # 8
  # 1 8 6 4 2 3 5 7

  idx = 1
  for num in nums:
    if num == idx:
      idx = idx + 1
      continue

    while True:
      if stack[-1] == idx:
        stack.pop()
        idx = idx + 1
      else:
        break

    stack.append(num)
    continue

  for _ in range(n - idx + 1):
    if stack[-1] == idx:
      stack.pop()
      idx = idx + 1
      continue
    else:
      print("Sad")
      exit()

  if stack[-1] == 0:
    print("Nice")
