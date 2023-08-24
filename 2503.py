import sys; input = sys.stdin.readline
from itertools import combinations, permutations
if __name__ == '__main__':

  n = int(input())
  predict_list = [list(map(int, input().split())) for _ in range(n)]

  # 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수의 list 생성
  answer_list = []
  for comb in combinations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3):
    for perm in permutations((0, 1, 2), 3):
      answer_list.append([comb[perm[0]], comb[perm[1]], comb[perm[2]]])

  for predict in predict_list:
    p_num, s, b = list(map(int, str(predict[0]))), predict[1], predict[2]

    # 질문한 세 자리 수 위에서 생성한 세 자리 수를 비교
    idx = 0
    while True:
      if idx > len(answer_list) - 1:
        break

      a_num = answer_list[idx]

      # 스트라이크 카운트
      tmp_s = 0
      for i in range(3):
        if p_num[i] == a_num[i]:
          tmp_s = tmp_s + 1

      # 볼 카운트
      tmp_b = len(set(p_num) & set(a_num)) - tmp_s

      if s == tmp_s and b == tmp_b:
        idx = idx + 1
      else:
        # 스트라이크와 볼의 개수가 같지 않은 세 자리 수는 answer_list에서 제거
        answer_list.pop(idx)

  print(len(answer_list))
