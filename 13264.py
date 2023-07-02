import sys; input = sys.stdin.readline
if __name__ == '__main__':

  def sa(string):
    lank_list = [i for i in range(l)]
    sa_list, temp_list = [0] * (l + 1), [0] * (l + 1)
    for i in range(l):
      sa_list[i] = ord(string[i])

    n = 1
    while n < l:
      lank_list.sort(key=lambda x: (sa_list[x], sa_list[min(x + n, l)]))

      for i in range(1, l):
        a, b = lank_list[i - 1], lank_list[i]
        if sa_list[a] != sa_list[b] or sa_list[min(a + n, l)] != sa_list[min(b + n, l)]:
          temp_list[b] = temp_list[a] + 1
        else:
          temp_list[b] = temp_list[a]

      sa_list = temp_list[:]
      n = n * 2
    return lank_list, sa_list

  string = str(input().rstrip())
  l = len(string)

  if l == 1:
    print(0)
  else:
    lank_list, sa_list = sa(string)
    print(*lank_list, sep="\n")
