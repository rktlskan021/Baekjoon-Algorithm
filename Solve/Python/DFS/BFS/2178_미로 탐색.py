from collections import deque

n, m = map(int, input().split())
M = []
for _ in range(n):
    M.append(list(map(int, input())))

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m and M[nx][ny] == 1:
                M[nx][ny] = M[x][y] + 1
                queue.append((nx, ny))


BFS(0, 0)
print(M[n-1][m-1])