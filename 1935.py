import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  expression = list(str(input()).rstrip())
  nums = [float(input()) for _ in range(n)]

  i = 2
  while len(expression) >= 3:

    print("--- before ---")
    print("i: ", i)
    print("expression: ", expression)
    print("nums: ", nums)

    if expression[i].isalpha():
      i = i + 1
    else:
      if expression[i] == '+':
        nums.append(nums[ord(expression.pop(i - 2)) - 65] + nums[ord(expression.pop(i - 2)) - 65])
      elif expression[i] == '-':
        nums.append(nums[ord(expression.pop(i - 2)) - 65] - nums[ord(expression.pop(i - 2)) - 65])
      elif expression[i] == '*':
        nums.append(nums[ord(expression.pop(i - 2)) - 65] * nums[ord(expression.pop(i - 2)) - 65])
      elif expression[i] == '/':
        nums.append(nums[ord(expression.pop(i - 2)) - 65] / nums[ord(expression.pop(i - 2)) - 65])
      expression[i - 2] = chr(len(nums) - 1 + 65)
      i = i - 2

    print("--- after ---")
    print("i: ", i)
    print("expression: ", expression)
    print("nums: ", nums)

  print()
  print("=== answer ===")
  print("{:.2f}".format(nums[-1]))
