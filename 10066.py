import sys; input = sys.stdin.readline
if __name__ == '__main__':

  def longest_palindrome(s):
    def expand(s, left, right):
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
      pal1 = expand(s, i, i)
      pal2 = expand(s, i, i + 1)
      longest = max(longest, pal1, pal2, key=len)

    return longest

  s = str(input().rstrip())
  lp = longest_palindrome(s)
  print(len(lp))
