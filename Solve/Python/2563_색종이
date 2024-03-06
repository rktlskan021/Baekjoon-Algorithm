import sys
input = sys.stdin.readline
  
drawing_paper = [[0 for _ in range(100)] for __ in range(100)]
t = int(input())
area = 0
for _ in range(t):
  l, b = map(int, input().split())
  for i in range(10):
    for j in range(10):
      drawing_paper[b+i][l+j] = 1

for _ in drawing_paper:
  area += _.count(1)
print(area)
