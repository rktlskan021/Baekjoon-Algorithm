import sys
input = sys.stdin.readline
n = int(input())

arr = [0] * n
for i in range(n):
    arr[i] = int(input())

dp = [0] * n

if n <= 2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

    print(max(dp))

'''
잔을 최대 2잔까지 마실 수 있기 때문에 1번이나 2번 음료는 무조건 먹을 수 밖에 없음.
1, 2, 4
1, 3, 4
2, 3, 5
dp[i] -> 1 ~ i잔에서의 가장 많은 포도주 양
dp[i] = max(arr[i] + arr[i-1], dp[i-1])
'''