import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = input().rstrip()
  answer = [0] * 9

  for i in n:
    num = int(i)

    if num == 9:
      num = 6

    answer[num] += 1

  answer[6] = (answer[6] + 1) // 2
  print(max(answer))
