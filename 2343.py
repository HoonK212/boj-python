import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
# import itertools
if __name__ == '__main__':

  n, m = map(int, input().split())
  nums = list(map(int, input().split()))
  # mean = sum(nums) / m
  #
  # combs = list(itertools.combinations(range(1, n), m - 1))
  # min_variance = 1e9
  # ans = 0
  #
  # for comb in combs:
  #   vals = []
  #   before = 0
  #   for c in comb:
  #     vals.append(sum(nums[before:c]))
  #     before = c
  #   vals.append(sum(nums[before:]))
  #
  #   vsum = 0
  #   for val in vals:
  #     vsum += (val - mean) ** 2
  #   variance = vsum / m
  #
  #   if variance < min_variance:
  #     min_variance = variance
  #     ans = max(vals)
  #
  # print(ans)

  l, r = max(nums), sum(nums)  # 가능한 블루레이의 크기 범위 설정
  ans = 0

  while l <= r:
    mid = (l + r) // 2 # mid: 블루레이 크기
    sum, cnt = 0, 0 # sum: 현재 블루레이에 담긴 강의의 길이 합, cnt: 사용된 블루레이 개수

    for i in range(n):
      if sum + nums[i] > mid: # 강의를 추가했을 때 mid를 초과한다면 새로운 블루레이에 추가해야 하므로 cnt를 증가시키고 sum을 초기화
        sum = 0
        cnt += 1
      sum += nums[i] # 현재 블루레이에 강의 추가

    if sum: # 남은 강의가 있으면 새로운 블루레이가 필요하므로, cnt += 1
      cnt += 1

    if cnt > m: # cnt가 m보다 크면 mid가 작다는 뜻이므로, l = mid + 1
      l = mid + 1
    else: # 그렇지 않으면, r = mid - 1
      r = mid - 1
      ans = mid

  print(ans)