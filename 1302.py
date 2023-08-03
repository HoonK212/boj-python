import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  titles = {}

  for _ in range(n):
    title = str(input().rstrip())

    if title in titles.keys():
      titles[title] += 1
    else:
      titles[title] = 1

  sorted_titles = sorted(titles.items(), key = lambda item : (-item[1], item[0]))
  print(sorted_titles[0][0])
