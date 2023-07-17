import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n, m = map(int, input().split())
  tree_list = list(map(int, input().split()))
  start, end = 0, max(tree_list)

  answer = 0

  # 이진 탐색을 위한 반복문과 start, end, mid 값 설정이 핵심 !!!
  while start <= end:
    mid = (start + end) // 2

    # total 계산
    total = 0
    for tree in tree_list:
      if tree > mid:
        total += tree - mid

    if total < m:
      # mid 값이 더 작아져야 하므로 end 재설정
      end = mid - 1
    else:
      # mid 값이 더 커져야 하므로 start 재설정
      start = mid + 1
      # m 이상이면서 최소한의 나무를 얻는 것이 목표이므로, 일단 answer에 현재 mid 값 대입
      answer = mid

  print(answer)
