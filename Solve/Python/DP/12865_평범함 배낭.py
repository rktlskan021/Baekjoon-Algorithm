import sys

N, K = map(int, sys.stdin.readline().split())
item = [] # (무게, 가치) [(6, 13), (4, 8), (3, 6), (5, 12)]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    item.append((W,V))

M = [[0] * (K+1) for i in range(N+1)]

for i in range(1, len(M)): # i : 보석의 개수
    for j in range(len(M[i])):
        if item[i-1][0] <= j:
            if item[i-1][1] + M[i-1][j-item[i-1][0]] > M[i-1][j]:
                M[i][j] = item[i-1][1] + M[i-1][j-item[i-1][0]]
            else:
                M[i][j] = M[i-1][j]
        else:
            M[i][j] = M[i-1][j]

print(M[N][K])

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# info = []
# for _ in range(n):
#     w, v = map(int, input().split())
#     info.append((w, v))

# dp = [[0] * (k+1) for _ in range(n+1)]

# for i in range(1, n + 1):
#     w, v = info[i-1]
#     for j in range(1, k+1):
#         if w <= j:
#             dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
#         else:
#             dp[i][j] = dp[i-1][j]

# print(dp[n][k])