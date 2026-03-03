import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

m, n = len(a), len(b)

# dp = [[-1] * n for _ in range(m)]

# def S(i, j):
#     if i < 0 or j < 0: return 0
#     if dp[i][j] != -1: return dp[i][j]

#     if a[i] == b[j]:
#         dp[i][j] = S(i-1, j-1) + 1
#     else: dp[i][j] = max(S(i-1, j), S(i, j-1))

#     return dp[i][j]

# print(S(m-1, n-1))

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m):
    for j in range(n):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m - 1][n - 1])