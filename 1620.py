import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n, m = map(int, input().split())
  pokemons = {} # n과 m의 최대값이 99,999이므로 list가 아닌 dict 사용
  for i in range(1, n + 1):
    pokemon = str(input().rstrip())
    pokemons[i] = pokemon
    pokemons[pokemon] = i

  for _ in range(m):
    target = str(input().rstrip())
    if target.isdigit():
      print(pokemons[int(target)])
    else:
      print(pokemons[target])