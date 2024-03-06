import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  num, c = map(int, input().split())
  nums = list(map(int, input().split()))
  cnt = {}
  for i, num in enumerate(nums):
    if num in cnt:
      cnt[num][0] += 1
    else:
      cnt[num] = [1, i, num]

  frequency = sorted(cnt.values(), key=lambda x: (-x[0], x[1]))

  answer = []
  for f in frequency:
    answer += [f[2]] * f[0]
  print(*answer)