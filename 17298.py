import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  n = int(input())
  nums = list(map(int, input().split()))
  stack = deque() # deque를 stack으로 사용

  answer = [-1] * n # -1을 default 값으로 초기화
  for i in range(n):
    while stack and nums[stack[-1]] < nums[i]: # 오큰수 찾기
      answer[stack.pop()] = nums[i]
    stack.append(i) # 오큰수를 찾았는지 여부와 무관하게 stack에 append

  print(*answer)
