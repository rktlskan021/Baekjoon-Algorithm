import sys
input = sys.stdin.readline

n = int(input())
M = [input().strip() for _ in range(n)] # strip()으로 줄바꿈 제거

visited = [[False] * n for _ in range(n)]
result = []

def isValidPos(x, y):
    # 범위 안에 있고, 집('1')이면서, 아직 방문하지 않은 곳인가?
    if 0 <= x < n and 0 <= y < n:
        if M[x][y] == '1' and not visited[x][y]:
            return True
    return False

def DFS(start_x, start_y):
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = True # 시작점 방문 처리
    c = 0

    while stack:
        x, y = stack.pop()
        c += 1
        
        # 상하좌우 탐색
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if isValidPos(nx, ny):
                visited[nx][ny] = True # 스택에 넣기 전에 즉시 방문 처리
                stack.append((nx, ny))
    return c

# 전체 지도 순회
for i in range(n):
    for j in range(n):
        if isValidPos(i, j):
            # 방문하지 않은 집을 발견할 때마다 새로운 단지 DFS 시작
            result.append(DFS(i, j))

# 결과 출력
print(len(result))
result.sort()
for count in result:
    print(count)