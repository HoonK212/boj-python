import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  def sa(string):
    lank_list = [i for i in range(l)]
    sa_list, temp_list = [0] * (l + 1), [0] * (l + 1)
    for i in range(l):
      sa_list[i] = ord(string[i])

    # sa_list[l] = -1
    # temp_list[lank_list[0]] = 0
    # temp_list[l] = -1
    print(lank_list)
    print(sa_list)
    print(temp_list, "\n")

    n = 1
    while n < l:
      lank_list.sort(key=lambda x: (sa_list[x], sa_list[min(x + n, l)]))
      print("lank_list sort: ", lank_list, "\n")

      for i in range(1, l):
        a, b = lank_list[i - 1], lank_list[i]
        if sa_list[a] != sa_list[b] or sa_list[min(a + n, l)] != sa_list[min(b + n, l)]:
          temp_list[b] = temp_list[a] + 1
        else:
          temp_list[b] = temp_list[a]
      print("for문 종료 / temp_list: ", temp_list, "\n")

      # if temp_list[l - 1] == l - 1:
      #   sa_list = temp_list[:]
      #   print("if문 내부 / sa_list: ", sa_list, "\n")
      #   break

      sa_list = temp_list[:]
      n = n * 2
      print("sa 마지막 줄 / sa_list: ", sa_list, "\n")
    return lank_list, sa_list

  def lcp(string, lank_list, sa_list):
    length = 0
    lcp_list = [0] * l
    for i in range(l):
      n = sa_list[i]

      # if n == 0:
      #   continue

      m = lank_list[n - 1]
      while i + length < l and m + length < l and string[i + length] == string[m + length]:
        length += 1

      lcp_list[n] = length
      if length:
        length -= 1
      print("lcp 마지막 줄 / lcp_list: ", lcp_list, "\n")
    return lcp_list

  l = int(input())
  string = str(input())

  if l == 1:
    print(0)
  else:
    lank_list, sa_list = sa(string)
    lcp_list = lcp(string, lank_list, sa_list)
    print(max(lcp_list))
