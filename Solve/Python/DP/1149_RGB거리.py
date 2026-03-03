import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n = int(input())

prices = []
for i in range(n):
    prices.append(list(map(int, input().split())))

# dp = [[0,0,0] for _ in range(n)]

# dp[0][0] = prices[0][0]
# dp[0][1] = prices[0][1]
# dp[0][2] = prices[0][2]

# for i in range(1, n):
#     dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + prices[i][0]
#     dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + prices[i][1]
#     dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + prices[i][2]

# print(min(dp[n-1]))

dp = [[-1, -1, -1] for _ in range(n)]
def rgb(n, color):
    colors = [0, 1, 2]
    if n == 0: return prices[0][color]
    if dp[n][color] != -1: return dp[n][color]

    colors.remove(color)
    dp[n][color] = prices[n][color] + min(rgb(n-1, colors[0]), rgb(n-1, colors[1]))

    return dp[n][color]

print(min(rgb(n-1, 0), rgb(n-1, 1), rgb(n-1, 2)))