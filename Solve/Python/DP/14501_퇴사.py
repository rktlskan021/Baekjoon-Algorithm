# import sys
# input = sys.stdin.readline
# n = int(input())

# schedules = []
# for _ in range(n):
#     t, p = map(int, input().split())
#     schedules.append((t, p))

# dp = [0] * (n + 1)
# if schedules[n-1][0] == 1: dp[n-1] = schedules[n-1][1]

# for i in range(n-2, -1, -1):
#     t, p = schedules[i]
#     if t + i > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(dp[i + 1], p + dp[i + t])

# print(max(dp))

import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

max_profit = 0

def dfs(day, current_profit):
    global max_profit
    
    # 기저 사례: 퇴사 날짜에 도달하거나 넘어간 경우
    if day >= n:
        max_profit = max(max_profit, current_profit)
        return

    # 1. 오늘 상담을 하는 경우 (퇴사 전까지 끝날 때만 가능)
    if day + t[day] <= n:
        dfs(day + t[day], current_profit + p[day])
    
    # 2. 오늘 상담을 안 하고 다음 날로 넘어가는 경우
    dfs(day + 1, current_profit)

dfs(0, 0)
print(max_profit)