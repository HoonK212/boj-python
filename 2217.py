import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  k = []
  for _ in range(n):
    k.append(int(input()))
  k.sort()

  answers = []
  for r in k:
    answers.append(r * n)
    n -= 1

  print(max(answers))
