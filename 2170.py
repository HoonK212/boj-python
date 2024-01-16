import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n = int(input())
  lines = [list(map(int, input().split())) for _ in range(n)]
  lines.sort()

  # 정렬된 line들 중 첫번째 line의 x, y를 start, end로 초기화
  start = lines[0][0]
  end = lines[0][1]

  answer = 0

  # 정렬된 line들 중 두번째 line부터 마지막 line까지 반복
  # x, y를 각각 cur_start, cur_end로 초기화
  for cur_start, cur_end in lines[1:]:

    # cur_start가 기존의 end보다 크면, start~end까지의 길이를 합산하고,
    # start를 cur_start로 초기화
    if cur_start > end:
      answer += end - start
      start = cur_start

    # 기존의 end와 cur_end 중, 큰 값으로 end 초기화
    end = max(end, cur_end)

  # 마지막으로 start~end까지의 길이 합산
  answer += end - start

  print(answer)
