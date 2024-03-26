import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  # def process(lst):
  #   idx_list = [lst.index(sorted(lst)[i]) for i in range(n)]
  #   result_list = [idx_list[0]]
  #   for idx in idx_list[1:]:
  #     if idx < result_list[-1]:
  #       result_list.append(idx)
  #   return result_list
  #
  # n = int(input())
  # road_lens = list(map(int, input().split()))
  # oil_prices = list(map(int, input().split()))
  #
  # processed_list = process(oil_prices)
  # ans = 0
  #
  # for i in processed_list:
  #   ans += oil_prices[i] * sum(road_lens[i:])
  #   road_lens =  road_lens[:i]
  #
  # print(ans)

  def find_min_cost(n, road_lens, oil_prices):
    min_price = oil_prices[0]
    total_cost = 0

    for i in range(n - 1):
      # 만약 현재 도시의 기름 가격이 최소 가격보다 저렴하다면, 최소 가격 갱신
      if oil_prices[i] < min_price:
        min_price = oil_prices[i]
      # 현재 도시의 가격(또는 최소 가격)으로 다음 도시까지 가는데 필요한 비용을 계산하고 총 비용에 합산
      total_cost += min_price * road_lens[i]

    return total_cost  # 최종 계산된 총 비용 반환

  n = int(input())
  road_lens = list(map(int, input().split()))
  oil_prices = list(map(int, input().split()))

  min_cost = find_min_cost(n, road_lens, oil_prices)

  print(min_cost)