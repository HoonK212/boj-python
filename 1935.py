import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  expression = list(str(input()).rstrip())
  nums = [int(input()) for _ in range(n)]

  i = 2
  while len(expression) >= 3:
    if expression[i].isnumeric() or expression[i].isalpha():
      i = i + 1
    else:
      if expression[i] == '+':
        expression[i] = nums[i - 2] + nums[i -1]
      elif expression[i] == '-':
        expression[i] = nums[i - 2] - nums[i -1]
      elif expression[i] == '*':
        expression[i] = nums[i - 2] * nums[i -1]
      elif expression[i] == '/':
        expression[i] = nums[i - 2] / nums[i -1]
      expression.pop(i - 2)
      expression.pop(i - 2)
      i = i -2

  print(expression[0])
