import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    N = int(input())
    dp = [0, 1, 1, 1, 2, 2] + ([-1] * N)
    if dp[N] != -1:
        print(dp[N])
        continue
    for i in range(6, N+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    print(dp[N])