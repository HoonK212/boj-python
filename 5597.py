import sys; input = sys.stdin.readline
if __name__ == '__main__':

  answer = [i for i in range(1, 31)]

  for _ in range(28):
    student = int(input())
    answer.remove(student)

  print(min(answer))
  print(max(answer))
