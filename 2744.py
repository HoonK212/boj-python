import sys; input = sys.stdin.readline
if __name__ == '__main__':

  string = str(input()).rstrip()

  for char in string:
    num = ord(char)
    print(chr(num + 32), end='') if 65 <= num <= 90 else print(chr(num - 32), end='')
