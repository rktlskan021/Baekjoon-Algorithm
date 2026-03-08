import sys
input = sys.stdin.readline

n, c = map(int, input().split())
coors = [0] * n

for i in range(n):
    coors[i] = int(input())

coors.sort()
left = 1
right = coors[n-1] - coors[0]

result = 0
while left <= right:
    mid = (left + right) // 2

    total = 1
    start = coors[0]
    for i in range(1, n):
        if coors[i] - start >= mid:
            total += 1
            start = coors[i]
    
    if total >= c:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)