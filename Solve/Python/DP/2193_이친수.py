import sys
input = sys.stdin.readline
n = int(input())

dp = [[0, 0] for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))

'''
n == 1
1

n == 2
10

n == 3
100 101

n == 4
1000 1001 1010

n == 5
10000 10001 10100 10101 10010

n == 6
100000 100001 100100 100101 101000 101001 101010 100010

0으로 끝나는거는 2배
1로 끝나는거는 1개

'''