import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import heapq
if __name__ == '__main__':

  n = int(input())

  leftHeap = [] # 왼쪽 힙 (최대 힙으로 사용하기 위해 부호를 반대로 저장) 초기화
  rightHeap = [] # 오른쪽 힙 (최소 힙)을 초기화
  answer = []

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

  for ans in answer:
    print(ans)