import sys; input = sys.stdin.readline
if __name__ == '__main__':

  s = str(input().rstrip())
  answer = []

  for i in range(len(s)):
    answer.append(s[i:])

  answer.sort()
  print(*answer, sep="\n")
