import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n, m = map(int, input().split())
  graph = [list(str(input().rstrip())) for _ in range(n)]

  answer = []
  for i in range(n - 7):
    for j in range(m - 7):
      # W로 칠하는 갯수와 B로 칠하는 갯수를 같이 카운팅 하는 것이 핵심 !!!
      w_cnt, b_cnt = 0, 0

      for k in range(i, i + 8):
        for l in range(j, j + 8):
          if (k + l) % 2 == 0: # (k + l)이 짝수
            if graph[k][l] == 'W':
              b_cnt += 1
            else:
              w_cnt += 1
          else: # (k + l)이 홀수
            if graph[k][l] == 'W':
              w_cnt += 1
            else:
              b_cnt += 1

      answer.append(w_cnt)
      answer.append(b_cnt)

  print(min(answer))
