import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  answer = []

  while True:
    stack = []
    cnt = 0

    s = input()
    if '-' in s:
      break

    for i in range(len(s)):
      if not stack and s[i] == '}':
        cnt += 1
        stack.append('{')
      elif stack and s[i] == '}':
        stack.pop()
      else:
        stack.append(s[i])

    cnt += len(stack) // 2
    answer.append(cnt)

  for i in range(len(answer)):
    print(i + 1, answer[i], sep='. ')
