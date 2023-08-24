import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())

  zero_flag = False # 0은 존재 여부만 중요
  one_cnt = 0 # 1은 개수만 중요
  negative_nums = [] # 음수 리스트
  positive_nums = [] # (1을 제외한) 양수 리스트

  for _ in range(n):
    num = int(input())
    if num == 0:
      zero_flag = True
      continue
    if num == 1:
      one_cnt = one_cnt + 1
      continue
    if num < 0:
      negative_nums.append(num)
      continue
    if num > 1:
      positive_nums.append(num)
      continue

  # 음수와 양수 리스트 모두 절대값이 큰 수가 앞으로 오도록 정렬
  negative_nums.sort()
  positive_nums.sort(reverse=True)

  tmp = 0
  answer = one_cnt # 1의 개수로 초기화하며 answer 계산 시작

  # 절대값이 큰 순서대로 음수를 두 개씩 묶어, 최대한 큰 양수로 만든 뒤 answer에 합산
  for idx, n_num in enumerate(negative_nums):
    if tmp == 0:
      # negative_nums의 길이가 홀수인 경우, 절대값이 가장 작은 음수는 양수로 만들 방법이 없기 때문에
      #   0이 존재했다면 0과 묶어 0으로 만듦
      #   0이 존재하지 않았다면 다른 수와 묶지 않고 answer에 합산
      if idx == len(negative_nums) - 1:
        if not zero_flag:
          answer = answer + n_num
        break
      else:
        tmp = n_num
        continue
    if tmp != 0:
      answer = answer + (tmp * n_num)
      tmp = 0
      continue

  # 절대값이 큰 순서대로 양수를 두 개씩 묶어, 최대한 수로 만든 뒤 answer에 합산
  for idx, p_num in enumerate(positive_nums):
    if tmp == 0:
      # positive_nums의 길이가 홀수인 경우, 가장 작은 양수는 다른 수와 묶지 않고 answer에 합산
      if idx == len(positive_nums) - 1:
        answer = answer + p_num
        break
      else:
        tmp = p_num
        continue
    if tmp != 0:
      answer = answer + (tmp * p_num)
      tmp = 0
      continue

  print(answer)
