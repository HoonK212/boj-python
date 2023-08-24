import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  expression = list(str(input()).rstrip())
  nums = [float(input()) for _ in range(n)]

  # 선입후출의 개념을 적용하는 것이 핵심 !!!
  stack = []
  for char in expression:
    if 'A' <= char <= 'Z':
      stack.append(nums[ord(char) - ord('A')])
    else:
      b = stack.pop()
      a = stack.pop()
      if char == '+':
        stack.append(a + b)
      elif char == '-':
        stack.append(a - b)
      elif char == '*':
        stack.append(a * b)
      elif char == '/':
        stack.append(a / b)

  print("{:.2f}".format(stack[0]))
