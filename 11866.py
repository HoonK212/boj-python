import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n, k = map(int, input().split())
  nums = [i + 1 for i in range(n)]

  idx = 0
  answer = []

  for _ in range(n):
    # k값과 nums list의 길이를 이용해 idx값을 찾는 것이 핵심 !!!
    idx = (idx + k - 1) % len(nums)
    answer.append(nums.pop(idx))

  print("<", end="")
  print(*answer, sep=", ", end=">")
