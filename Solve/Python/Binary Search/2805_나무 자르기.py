import sys

input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

result = 0
while left <= right:
    mid = (right + left) // 2

    h = 0
    for tree in trees:
        if tree > mid:
            h += tree - mid

    if h >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)