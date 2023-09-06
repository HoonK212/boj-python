import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  def sa(string):
    sa_list = [i for i in range(l)]
    lank_list, tmp_list = [0] * (l + 1), [0] * (l + 1)
    for i in range(l):
      lank_list[i] = ord(string[i])

    lank_list[l] = -1
    tmp_list[l] = -1

    n = 1
    while n < l:
      sa_list.sort(key=lambda x: (lank_list[x], lank_list[min(x + n, l)]))

      for i in range(1, l):
        a, b = sa_list[i - 1], sa_list[i]
        if lank_list[a] != lank_list[b] or lank_list[min(a + n, l)] != lank_list[min(b + n, l)]:
          tmp_list[b] = tmp_list[a] + 1
        else:
          tmp_list[b] = tmp_list[a]

      lank_list = tmp_list[:]
      n = n * 2
    return sa_list, lank_list

  def lcp(string, sa_list, lank_list):
    length = 0
    lcp_list = [0] * l
    for i in range(l):
      n = lank_list[i]

      m = sa_list[n - 1]
      while i + length < l and m + length < l and string[i + length] == string[m + length]:
        length += 1

      lcp_list[n] = length
      if length:
        length -= 1
    return lcp_list

  l = int(input())
  string = str(input())

  if l == 1:
    print(0)
  else:
    sa_list, lank_list = sa(string)
    lcp_list = lcp(string, sa_list, lank_list)
    print(max(lcp_list))
