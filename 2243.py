import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def change(target, inc, idx, start, end):
    if target < start or end < target:
      return
    tree[idx] += inc # 사탕 개수 증가
    if start != end:
      change(target, inc, idx * 2, start, (start + end) // 2)
      change(target, inc, idx * 2 + 1, (start + end) // 2 + 1, end)


  def get(rank, idx, start, end):
    if start == end: # 리프 노드 도달
      return start
    else:
      if tree[idx * 2] >= rank: # 구간 합과 rank 비교
        return get(rank, idx * 2, start, (start + end) // 2)
      else:
        return get(rank - tree[idx * 2], idx * 2 + 1, (start + end) // 2 + 1, end)


  level = 1_000_000 # 맛 단계
  nums = [0] * (level + 1)
  tree = [0] * (level * 4)

  n = int(input())
  for _ in range(n):
    case, *content = map(int, input().split())

    if case == 1:
      # content[0]을 rank로, 꺼낼 사탕의 맛 단계에 해당하는 리프 노드 반환
      ans = get(content[0], 1, 1, level)
      print(ans)

      # get을 수행한대로, nums와 tree 수정
      nums[ans] -= 1
      change(ans, -1, 1, 1, level)

    elif case == 2:
      nums[content[0]] += content[1]
      change(content[0], content[1], 1, 1, level)