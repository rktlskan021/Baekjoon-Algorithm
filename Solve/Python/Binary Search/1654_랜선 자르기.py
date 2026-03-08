import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lan_cables = [0] * k
for i in range(k):
    lan_cables[i] = int(input())

left = 1
right = max(lan_cables)

result = 0
while left <= right:
    mid = (left + right) // 2

    total = 0
    for cable in lan_cables:
        if cable >= mid:
            total += cable // mid
    
    if total >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)