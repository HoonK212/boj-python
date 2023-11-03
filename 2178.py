import sys; input = sys.stdin.readline; sys.setrecursionlimit(10 ** 6)
from collections import deque

if __name__ == '__main__':

    n, m = map(int, input().split())
    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input())))


    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and coordinates[nx][ny] == 1:
                    queue.append((nx, ny))
                    coordinates[nx][ny] = coordinates[x][y] + 1

        return coordinates[n - 1][m - 1]


    print(bfs(0, 0))
