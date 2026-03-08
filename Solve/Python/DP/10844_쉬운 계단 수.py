import sys
input = sys.stdin.readline
n = int(input())

dp = [[0] * 10 for _ in range(n)]

dp[0][0] = 0
for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n-1]) % 1000000000)

'''
길이가 1일 때
1
2
3
4
5
6
7
8
9

길이가 2일 때
10
21
12, 32
23, 43
34, 54
45, 54
56, 76
67, 87
78, 98
89

길이가 3일 때
210
121, 321, 101
212, 232, 432
123, 323, 343, 543
234, 254, 434, 454
45, 54
56, 76
67, 87
78, 98
789, 989



'''