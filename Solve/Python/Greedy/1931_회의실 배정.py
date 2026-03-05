import sys
input = sys.stdin.readline
n = int(input())

meetings = []
for i in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda m: (m[1], m[0]))

count = 0
e = 0

for ns, ne in meetings:
    if e > ns:
        continue

    count += 1
    e = ne

print(count)