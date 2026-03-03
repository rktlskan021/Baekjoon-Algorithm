import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]] + [0] * (n - 1)

for i in range(1, len(nums)):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))

sys.setrecursionlimit(10000000)
# dp = [-1] * n
# dp[0] = nums[0]

# def a(n):
#     if n == 0: return dp[0]
#     if dp[n] != -1: return dp[n]

#     dp[n] = max(a(n-1) + nums[n], nums[n])
#     return dp[n]

# a(n-1)
# print(max(dp))



'''
1 ~ 10
max(1, 9~10)

'''
