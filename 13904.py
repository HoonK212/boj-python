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

  # 마감일 역순으로 for문을 돌며 heapq를 사용하는 것이 핵심 !!!
  for d in range(max_d, 0, -1):
    for w in assignments[d]:
      heapq.heappush(heap, -w)
    if heap:
      answer = answer + -heapq.heappop(heap)

  print(answer)
