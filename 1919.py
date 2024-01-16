import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  # string a와 b 입력
  str_a = str(input().rstrip())
  str_b = str(input().rstrip())

  # 각 알파벳 철자에 해당하는 arr 배열 생성
  arr = [0] * 26

  # string a의 각 철자에 알맞는 i번째 배열 값 +=1
  for a in str_a:
    i = ord(a) - 97
    arr[i] += 1

  # string b의 각 철자에 알맞는 i번째 배열 값 -=1
  for b in str_b:
    i = ord(b) - 97
    arr[i] -= 1

  answer = 0

  # 여전히 arr 배열에서 0이 아닌 값들은 애너그램 관계를 불가능하게 만드는 비대칭 철자의 수
  for i in arr:
    answer += abs(i) # 해당 값들을 절대값으로 합산

  print(answer)
