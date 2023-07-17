import sys; input = sys.stdin.readline
if __name__ == '__main__':

  score, answer = 0, 0

  for _ in range(10):
    score += int(input())

    # 100 - answer의 값이 100 - score의 절대값보다 작아질 때까지 answer에 누적 score를 대입하는 것이 핵심 !!!
    if 100 - answer >= abs(100 - score):
      answer = score

    # score가 100보다 크다면 마지막 대소관계 비교(위 if문 로직) 후, 루프 종료
    if score > 100:
      break

  print(answer)
