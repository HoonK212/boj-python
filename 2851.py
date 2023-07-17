import sys; input = sys.stdin.readline
if __name__ == '__main__':

  score, answer = 0, 0

  for _ in range(10):
    score += int(input())

    if 100 - answer >= abs(100 - score):
      answer = score

    if score > 100: break

  print(answer)
