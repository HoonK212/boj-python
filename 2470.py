import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n = int(input())
  nums = sorted(list(map(int, input().split())))

  # 투 포인트 초기화
  l = 0
  r = n - 1

  tmp = 2e9 # 최대 1,999,999,999가 가능하므로 2,000,000,000으로 초기화
  answer = []

  while l < r:
    l_num = nums[l]
    r_num = nums[r]
    sum = l_num + r_num

    if abs(sum) < tmp:
      tmp = abs(sum)
      answer = [l_num, r_num]
      if tmp ==0: # 특성값이 0이 되는 두 용액을 찾으면 break
        break

    if sum < 0:
      l += 1
    else:
      r -= 1

  print(*answer)