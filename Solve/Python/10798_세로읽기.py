import sys
input = sys.stdin.readline
arr = []
m = 0
for _ in range(5):
  tmp = list(input())
  tmp.pop(-1)
  if len(tmp) > m:
    m = len(tmp)
  arr.append(tmp)

for i in range(m):
  for j in range(5):
    if len(arr[j]) < (i + 1):
      continue
    print(arr[j][i], end="")
