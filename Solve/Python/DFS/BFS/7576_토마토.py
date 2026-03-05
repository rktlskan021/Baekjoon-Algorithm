import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))

zero = False
for i in M:
    for j in i:
        if j == 0: zero = True

def BFS():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if M[nx][ny] > 0 or M[nx][ny] == -1:
                    continue
                queue.append((nx, ny))
                M[nx][ny] = M[x][y] + 1

if not zero:
    print(0)

else:
    queue = deque()
    for i in range(n):
        for j in range(m):
            if M[i][j] == 1:
                queue.append((i, j))
            
    BFS()

    zero = False
    m = 0
    for i in M:
        for j in i:
            if j == 0: zero = True
            if j > m: m = j

    if zero:
        print(-1)
    else:
        print(m - 1)
