import sys; input = sys.stdin.readline
import heapq
if __name__ == '__main__':

  n = int(input())
  assignments = [[] for _ in range(1001)]
  max_d = 0

  for _ in range(n):
    d, w = map(int, input().split())
    assignments[d].append(w)
    max_d = max(max_d, d)

  heap = []
  answer = 0

  # 마감일이 늦은 날부터 시작해서 과제를 선택
  for d in range(max_d, 0, -1):
    # 현재 날짜에 해당하는 과제들을 힙에 추가
    for w in assignments[d]:
      heapq.heappush(heap, -w)  # 힙에는 점수의 음수를 저장 (최대 힙 구현)
    # 이 날짜에 할 수 있는 과제 중 가장 점수가 높은 과제를 선택
    if heap:
      answer = answer + -heapq.heappop(heap)  # 가장 점수가 높은 과제 추출 (저장된 음수값을 다시 양수로 변환)

  print(answer)
