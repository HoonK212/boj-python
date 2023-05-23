import sys; input = sys.stdin.readline; sys.setrecursionlimit(10 ** 6)
from collections import deque

if __name__ == '__main__':

    def bfs(i, j, graph, costs):
        queue = deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    # 더 작은 cost가 가능한 경우에만 cost를 update하는 것이 핵심 !!!
                    if costs[x][y] + graph[nx][ny] < costs[nx][ny]:
                        costs[nx][ny] = costs[x][y] + graph[nx][ny]
                        queue.append((nx, ny))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    inf = int(1e9)

    cnt = 1
    while True:
        n = int(input())
        if n == 0:
            break

        coordinates = []
        for _ in range(n):
            coordinates.append(list(map(int, input().split())))

        # 더 작은 cost를 찾아 update 하기 위해 costs를 최대값으로 초기화
        costs = [[inf] * n for _ in range(n)]
        costs[0][0] = coordinates[0][0]

        bfs(0, 0, coordinates, costs)

        # bfs 연산이 완료된 후, costs[i][j]는 (i, j)까지 도달하기 위한 가장 작은 cost를 의미
        #   해당 문제는 제일 오른쪽 아래 칸까지 이동해야 하므로, costs[n - 1][n - 1]을 출력
        print(f'Problem {cnt}: {costs[n - 1][n - 1]}')
        cnt += 1
