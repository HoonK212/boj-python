import sys; input = sys.stdin.readline; sys.setrecursionlimit(10 ** 6)
from collections import deque
if __name__ == '__main__':

    m, n = map(int, input().split())
    coordinates = [list(map(int, input())) for _ in range(n)]

    answer = [[-1] * m for _ in range(n)]
    answer[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:

                if answer[nx][ny] == -1:

                    if coordinates[nx][ny] == 0:
                        answer[nx][ny] = answer[x][y]
                        queue.appendleft((nx, ny))

                    else:
                        answer[nx][ny] = answer[x][y] + 1
                        queue.append((nx, ny))

    print(answer[n - 1][m - 1])
