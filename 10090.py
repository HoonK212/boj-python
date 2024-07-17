import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from math import ceil, log2
if __name__ == '__main__':

  # 문제
  # 정수 1부터 n까지의 순열은 각각의 정수가 정확히 한 번씩 나타나는 a1, a2, ..., an의 시퀀스입니다.
  # 순열에서 두 정수가 더 큰 수가 더 작은 수 앞에 있을 때, 이 두 정수는 역전을 형성합니다.
  # 예를 들어, 순열 4 2 7 1 5 6 3에서는 총 10개의 역전이 있습니다. 다음 쌍들이 역전입니다.
  # 4-2, 4-1, 4-3, 2-1, 7-1, 7-5, 7-6, 7-3, 5-3, 6-3
  # 주어진 순열에서 역전의 개수를 계산하는 프로그램 invcnt를 작성하세요.
  #
  # 입력
  # 표준 입력의 첫 번째 줄에 n의 값이 주어집니다. 두 번째 줄에는 공백으로 구분된 n개의 숫자가 순열로 주어집니다.
  #
  # 출력
  # 표준 출력에 역전의 개수를 출력하세요.
  #
  # 제한
  # 2 ≤ n ≤ 1000000

  def find(start, end, left, right, node):
    """
    세그먼트 트리에서 주어진 범위의 합을 구하는 함수
    :param start: 현재 노드의 시작 범위
    :param end: 현재 노드의 끝 범위
    :param left: 쿼리의 시작 범위
    :param right: 쿼리의 끝 범위
    :param node: 현재 노드의 인덱스
    :return: 주어진 범위의 합
    """
    if start > right or end < left:  # 쿼리 범위 밖인 경우
      return 0
    if left <= start and end <= right:  # 현재 노드의 범위가 쿼리 범위에 완전히 포함되는 경우
      return tree[node]
    mid = (start + end) // 2  # 중간 지점 계산
    # 왼쪽과 오른쪽 자식 노드로 재귀적으로 합을 구함
    return find(start, mid, left, right, node * 2) + find(mid + 1, end, left, right, node * 2 + 1)


  def update(node):
    """
    세그먼트 트리의 특정 노드를 업데이트하는 함수
    :param node: 업데이트할 노드 (실제 값이 아니라 순열 값)
    """
    temp = size + node - 1  # 리프 노드의 위치 계산
    while temp >= 1:  # 루트 노드까지 업데이트
      tree[temp] += 1
      temp //= 2  # 부모 노드로 이동

    # 입력값 받기


  n = int(input())
  data = list(map(int, input().split()))

  # 세그먼트 트리 초기화
  # n의 최댓값이 1000000이므로 이를 커버할 수 있는 트리 크기를 설정
  size = 2 ** ceil(log2(1000000))
  tree = [0] * (size * 2)
  ans = 0

  # 역전 쌍 계산
  for i in data:
    # 현재 숫자보다 큰 숫자들이 오른쪽에 몇 개 있는지 찾기
    ans += find(1, size, i + 1, n, 1)
    # 현재 숫자를 트리에 업데이트
    update(i)

  print(ans)