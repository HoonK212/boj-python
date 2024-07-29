import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def judge(num):
    if num > 0:
      return 1
    elif num < 0:
      return -1
    else:
      return 0

  # 세그먼트 트리 업데이트 함수
  def update(start, end, index, changeIdx, changeNum):
    # 변경하려는 인덱스가 현재 노드의 범위를 벗어나면 종료
    if changeIdx < start or changeIdx > end:
      return
    # 리프 노드에 도달한 경우 값을 변경
    if start == end:
      tree[index] = changeNum
      return
    # 현재 노드의 범위를 반으로 나누어 재귀적으로 탐색
    mid = (start + end) // 2
    update(start, mid, index * 2, changeIdx, changeNum)
    update(mid + 1, end, index * 2 + 1, changeIdx, changeNum)
    # 자식 노드들의 곱을 현재 노드에 저장
    tree[index] = tree[index * 2] * tree[index * 2 + 1]

  # 세그먼트 트리 쿼리 함수 (구간 곱 계산)
  def query(start, end, index, left, right):
    # 쿼리 범위가 현재 노드의 범위와 전혀 겹치지 않으면 1 반환 (곱셈의 항등원)
    if left > end or right < start:
      return 1
    # 쿼리 범위가 현재 노드의 범위를 완전히 포함하면 현재 노드의 값 반환
    if left <= start and right >= end:
      return tree[index]
    # 현재 노드의 범위를 반으로 나누어 재귀적으로 탐색하고 결과를 곱함
    mid = (start + end) // 2
    return query(start, mid, index * 2, left, right) * query(mid + 1, end, index * 2 + 1, left, right)

  # 세그먼트 트리 초기화 함수
  def init(start, end, index):
    # 리프 노드에 도달한 경우
    if start == end:
      nodes[start] = judge(nodes[start])  # 원본 배열의 값을 1, -1, 0으로 변환
      tree[index] = nodes[start]
      return tree[index]
    # 현재 노드의 범위를 반으로 나누어 재귀적으로 초기화
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)
    return tree[index]

  # 메인 로직
  while True:
    try:
      n, k = map(int, input().split())
      nodes = list(map(int, input().split()))

      tree = [0] * (n * 4)  # 세그먼트 트리
      answer = ""

      # 세그먼트 트리 초기화
      init(0, n - 1, 1)

      # k개의 명령 처리
      for _ in range(k):
        command = input().rstrip().split()
        if command[0] == 'C':  # 변경 명령
          i, V = int(command[1]), int(command[2])
          nodes[i - 1] = judge(V)  # 원본 배열 갱신
          update(0, n - 1, 1, i - 1, judge(V))  # 세그먼트 트리 업데이트
        else:  # 곱셈 명령
          i, j = int(command[1]), int(command[2])
          res = query(0, n - 1, 1, i - 1, j - 1)  # 구간 곱 계산
          # 결과에 따라 적절한 문자 추가
          if res == 0:
            answer += "0"
          elif res > 0:
            answer += "+"
          else:
            answer += "-"
      print(answer)  # 최종 결과 출력
    except Exception:
      break  # 입력이 끝나면 반복 종료