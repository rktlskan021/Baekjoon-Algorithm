import queue
import sys
input = sys.stdin.readline

n = int(input())
pair_num = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(pair_num):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)

# stack = [1]
# visited[1] = True
# count = 0

# while stack:
#     tmp = stack.pop()

#     for i in adj[tmp]:
#         if not visited[i]:
#             stack.append(i)
#             visited[i] = True
#             count += 1

q = queue.Queue()
q.put(1)
visited[1] = True
count = 0

while not q.empty():
    tmp = q.get()

    for i in adj[tmp]:
        if not visited[i]:
            q.put(i)
            count += 1
            visited[i] = True

print(count)