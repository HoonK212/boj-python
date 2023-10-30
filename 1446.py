import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n, d = map(int, input().split())
  shortcuts = [list(map(int, input().split())) for _ in range(n)]
  answer = [i for i in range(d + 1)]

  for i in range(d + 1):
    if i > 0:
      # '현재 위치까지의 거리'와 '앞선 위치까지의 거리 +1'을 비교해서 작은 값으로 초기화
      answer[i] = min(answer[i], answer[i - 1] + 1)

    for start, end, distance in shortcuts:
      # 현재 위치에 지름길의 시작점이 존재하면서, 지름길의 도착점이 고속대로 내에 존재하면서, 지름길을 활용할 때 거리가 더 짧으면
      if i == start and end <= d and answer[i] + distance < answer[end]:
        # '지름길의 도착점까지의 거리'를 '현재 위치까지의 거리' + '지름길의 거리'로 초기화
        answer[end] = answer[i] + distance

  print(answer[d])
