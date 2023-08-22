import sys; input = sys.stdin.readline
from collections import Counter
if __name__ == '__main__':

  n = int(input())
  nums = [int(input()) for _ in range(n)]
  nums.sort()
  counter_mc = Counter(nums).most_common(2) # 최빈값 계산을 위해 collections.Conter를 이용

  arithmetic_mean = sum(nums) / n
  median = nums[(n - 1) // 2]
  mode = counter_mc[0][0] if len(counter_mc) == 1 or counter_mc[0][1] != counter_mc[1][1] else counter_mc[1][0]
  difference = nums[-1] - nums[0]

  print(round(arithmetic_mean), median, mode, difference, sep="\n")
