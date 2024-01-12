import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  str_a = str(input().rstrip())
  str_b = str(input().rstrip())

  arr = [0] * 26
  for a in str_a:
    arr[ord(a) - 97] += 1
  for b in str_b:
    arr[ord(b) - 97] -= 1

  answer = 0
  for i in arr:
    answer += abs(i)

  print(answer)
