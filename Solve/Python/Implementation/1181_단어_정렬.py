import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for i in range(N):
    arr.add(input())

arr = list(arr)

arr.sort()
arr.sort(key=lambda x : len(x))

for i in arr:
    print(i, end="")