import sys; input = sys.stdin.readline
if __name__ == '__main__':

  num_list = [1, 1, 2, 2, 2, 8]
  pieces = list(map(int, input().split()))

  for idx, num in enumerate(num_list):
    print(num - pieces[idx], end=' ')
