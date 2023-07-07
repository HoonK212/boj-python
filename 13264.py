import sys; input = sys.stdin.readline
if __name__ == '__main__':

  def sa(string):
    sa_list = [i for i in range(l)]
    lank_list, temp_list = [0] * (l + 1), [0] * (l + 1)
    for i in range(l):
      lank_list[i] = ord(string[i])

    lank_list[l] = -1
    temp_list[l] = -1

    n = 1
    while n < l:
      sa_list.sort(key=lambda x: (lank_list[x], lank_list[min(x + n, l)]))

      for i in range(1, l):
        a, b = sa_list[i - 1], sa_list[i]
        if lank_list[a] != lank_list[b] or lank_list[min(a + n, l)] != lank_list[min(b + n, l)]:
          temp_list[b] = temp_list[a] + 1
        else:
          temp_list[b] = temp_list[a]

      lank_list = temp_list[:]
      n = n * 2
    return sa_list, lank_list

  string = str(input().rstrip())
  l = len(string)

  if l == 1:
    print(0)
  else:
    sa_list, lank_list = sa(string)
    print(*sa_list, sep="\n")
