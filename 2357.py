import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
import math
if __name__ == '__main__':

  # 세그먼트 트리 참고 링크: https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8-%ED%8A%B8%EB%A6%AC-Segment-Tree

  def make_seg(idx, start, end):
    if start == end: # 리프 노드
      seg[idx] = (nums[start], nums[start]) # 최소, 최대 동일
      return seg[idx]

    mid = (start + end) // 2

    left = make_seg(idx * 2, start, mid)
    right = make_seg(idx * 2 + 1, mid + 1, end)

    # min, max 계산
    seg[idx] = (min(left[0], right[0]), max(left[1], right[1]))

    return seg[idx]

  def find(idx, start, end):
    if r < start or l > end:
      return (1e9, 0) # 최대 min, 최소 max 반환

    if l <= start and end <= r:
      return seg[idx]

    mid = (start + end) // 2

    left = find(idx * 2, start, mid)
    right = find(idx * 2 + 1, mid + 1, end)

    # min, max 계산
    return (min(left[0], right[0]), max(left[1], right[1]))

  n, m = map(int, input().split())
  nums = list(int(input()) for _ in range(n))

  # 세그먼트 트리 depth 계산
  depth = math.ceil(math.log2(n)) + 1

  node_num = 1 << depth  ## (= 2^depth)
  seg = [0] * node_num

  make_seg(1, 0, n - 1)

  for _ in range(m):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1

    answer = find(1, 0, n - 1)
    print(answer[0], answer[1])
