import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(node):
    stack = [node]
    visited = [False] * (n + 1)
    result = []

    while stack:
        n_node = stack.pop()
        if visited[n_node]: continue
        visited[n_node] = True
        result.append(n_node)

        graph[n_node].sort(reverse=True)
        for num in graph[n_node]:
            if not visited[num]:
                stack.append(num)

    print(*result)

def BFS(node):
    queue = deque()
    queue.append(node)
    visited = [False] * (n + 1)
    result = []

    while queue:
        n_node = queue.popleft()
        if visited[n_node]: continue
        visited[n_node] = True
        result.append(n_node)

        graph[n_node].sort()
        for num in graph[n_node]:
            if not visited[num]:
                queue.append(num)

    print(*result)

DFS(v)
BFS(v)