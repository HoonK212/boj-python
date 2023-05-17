import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  s = input()
  if s[1] == '0':
    print(10 + int(s[2:]))
  else:
    print(int(s[0]) + int(s[1:]))
