import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n = int(input())
  lines = [list(map(int, input().split())) for _ in range(n)]
  lines.sort()

  start = lines[0][0]
  end = lines[0][1]
  answer = 0

  for cur_start, cur_end in lines[1:]:
    if cur_start > end:
      answer += end - start
      start = cur_start
    end = max(end, cur_end)
  answer += end - start

  print(answer)
