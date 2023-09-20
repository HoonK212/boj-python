import sys; input = sys.stdin.readline
if __name__ == '__main__':

  # source/53462915
  #   print(input().swapcase())

  string = str(input()).rstrip()

  for char in string:
    num = ord(char)
    print(chr(num + 32), end='') if 65 <= num <= 90 else print(chr(num - 32), end='')
