import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
for i in range(n):
    coins[i] = int(input())

coins.sort(reverse=True)
count = 0
for coin in coins:
    while coin <= k:
        count += k // coin
        k %= coin

print(count)