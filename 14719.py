import sys; input = sys.stdin.readline
if __name__ == '__main__':

  h, w = map(int, input().split())
  block = list(map(int, input().split()))
  answer = 0

  for i in range(1, w - 1): # 가장 왼쪽과 가장 오른쪽 제외
    # i를 기준으로, 왼쪽에서 가장 높은 블록과 오른쪽에서 가장 높은 블록의 높이를 비교하는 것이 핵심 !!!
    left = max(block[:i])
    right = max(block[i + 1:])

    # left와 right 중, 더 낮은 값과 block[i]의 차를 계산
    m = min(left, right)
    if m > block[i]:
      answer += m - block[i]

  print(answer)
