import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
  l = list(map(int, input().split()))
  arr.append(l)
tmp = 0
raw, col = 0, 0
for i, _ in enumerate(arr):
  if tmp < max(_):
    tmp = max(_)
    raw = i

print(tmp)
print(raw + 1, arr[raw].index(tmp) + 1)
