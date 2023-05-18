import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  s = input()
  if s[1] == '0':
    # A와 B 모두 0보다 크고 10보다 작거나 같기 때문에 s[1]이 0인 경우, A는 반드시 10
    print(10 + int(s[2:]))
  else:
    # A와 B 모두 0보다 크고 10보다 작거나 같기 때문에 s[1]이 0이 아닌 경우, A는 반드시 10보다 작음
    print(int(s[0]) + int(s[1:]))
