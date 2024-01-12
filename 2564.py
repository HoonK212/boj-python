import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def get_distance(x, y):
    if x == 1:
      return y
    if x == 2:
      return 2 * w + h - y
    if x == 3:
      return 2 * (w + h) - y
    if x == 4:
      return w + y


  w, h = map(int, input().split())
  n = int(input())

  distance = []
  for _ in range(n + 1):
    x, y = map(int, input().split())
    distance.append(get_distance(x, y))

  answer = 0
  for i in range(n):
    in_course = abs(distance[-1] - distance[i])
    out_course = 2 * (w + h) - in_course
    answer += min(in_course, out_course)

  print(answer)
