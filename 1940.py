import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n = int(input())
  m = int(input())
  nums = list(map(int, input().split()))
  nums.sort()

  # 2중 for문으로는 시간 제한에 걸리기 때문에, two pointer(start, end)로 구현하는 것이 핵심 !!!
  start, end = 0, len(nums) - 1
  cnt = 0

  while start < end:
    result = nums[start] + nums[end]
    if result > m:
      end -= 1
    elif result < m:
      start += 1
    else:
      cnt += 1
      start += 1
      end -= 1

  print(cnt)
