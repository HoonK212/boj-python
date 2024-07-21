import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import heapq
if __name__ == '__main__':

  n = int(input())

  # 두 개의 힙 초기화
  leftHeap = []  # 왼쪽 힙 (최대 힙으로 사용하기 위해 부호를 반대로 저장하는 것이 핵심 !!!)
  rightHeap = []  # 오른쪽 힙 (최소 힙)
  answer = []  # 결과를 저장할 리스트

  for _ in range(n):
    num = int(input())

    # 두 힙의 크기가 같으면 왼쪽 힙에 추가
    if len(leftHeap) == len(rightHeap):
      heapq.heappush(leftHeap, (-num, num))
    else:
      # 두 힙의 크기가 다르면 오른쪽 힙에 추가
      heapq.heappush(rightHeap, (num, num))

    # 오른쪽 힙이 비어있지 않고 왼쪽 힙의 최대값이 오른쪽 힙의 최소값보다 크다면
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
      # 왼쪽 힙의 최대값과 오른쪽 힙의 최소값을 교환
      min_val = heapq.heappop(rightHeap)[0]
      max_val = heapq.heappop(leftHeap)[1]
      heapq.heappush(leftHeap, (-min_val, min_val))
      heapq.heappush(rightHeap, (max_val, max_val))

    # 현재까지의 중간값을 결과 리스트에 추가
    answer.append(leftHeap[0][1])

  # 결과 출력
  for ans in answer:
    print(ans)

# 12
# 1
# 9
# 8
# 5
# 3
# 2
# 2
# 7
# 8
# 100
# 200
# 300

# 1
# 1
# 8
# 5
# 5
# 3
# 3
# 3
# 5
# 5
# 7
# 7

# [(-1, 1)]
# []
#
# [(-1, 1)]
# []
#
# [1]
#
# [(-1, 1)]
# [(9, 9)]
#
# [(-1, 1)]
# [(9, 9)]
#
# [1, 1]
#
# [(-8, 8), (-1, 1)]
# [(9, 9)]
#
# [(-8, 8), (-1, 1)]
# [(9, 9)]
#
# [1, 1, 8]
#
# [(-8, 8), (-1, 1)]
# [(5, 5), (9, 9)]
#
# [(-5, 5), (-1, 1)]
# [(8, 8), (9, 9)]
#
# [1, 1, 8, 5]
#
# [(-5, 5), (-3, 3), (-1, 1)]
# [(8, 8), (9, 9)]
#
# [(-5, 5), (-3, 3), (-1, 1)]
# [(8, 8), (9, 9)]
#
# [1, 1, 8, 5, 5]
#
# [(-5, 5), (-3, 3), (-1, 1)]
# [(2, 2), (8, 8), (9, 9)]
#
# [(-3, 3), (-2, 2), (-1, 1)]
# [(5, 5), (8, 8), (9, 9)]
#
# [1, 1, 8, 5, 5, 3]
#
# [(-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(5, 5), (8, 8), (9, 9)]
#
# [(-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(5, 5), (8, 8), (9, 9)]
#
# [1, 1, 8, 5, 5, 3, 3]
#
# [(-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(5, 5), (7, 7), (8, 8), (9, 9)]
#
# [(-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(5, 5), (7, 7), (8, 8), (9, 9)]
#
# [1, 1, 8, 5, 5, 3, 3, 3]
#
# [(-8, 8), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(5, 5), (7, 7), (8, 8), (9, 9)]
#
# [(-5, 5), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(7, 7), (8, 8), (8, 8), (9, 9)]
#
# [1, 1, 8, 5, 5, 3, 3, 3, 5]
#
# [(-5, 5), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(7, 7), (8, 8), (8, 8), (9, 9), (100, 100)]
#
# [(-5, 5), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(7, 7), (8, 8), (8, 8), (9, 9), (100, 100)]
#
# [1, 1, 8, 5, 5, 3, 3, 3, 5, 5]
#
# [(-200, 200), (-5, 5), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(7, 7), (8, 8), (8, 8), (9, 9), (100, 100)]
#
# [(-7, 7), (-5, 5), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(8, 8), (8, 8), (9, 9), (100, 100), (200, 200)]
#
# [1, 1, 8, 5, 5, 3, 3, 3, 5, 5, 7]
#
# [(-7, 7), (-5, 5), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(8, 8), (8, 8), (9, 9), (100, 100), (200, 200), (300, 300)]
#
# [(-7, 7), (-5, 5), (-3, 3), (-2, 2), (-2, 2), (-1, 1)]
# [(8, 8), (8, 8), (9, 9), (100, 100), (200, 200), (300, 300)]
#
# [1, 1, 8, 5, 5, 3, 3, 3, 5, 5, 7, 7]