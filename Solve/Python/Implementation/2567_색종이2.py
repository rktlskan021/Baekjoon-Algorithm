# 색종이 - 2
import sys

def checkRound(i, j, paper):
    global count
    check_X = [0, 0, 1, -1]
    check_Y = [1, -1, 0, 0]
    for k in range(4):
        if paper[i + check_X[k]][j + check_Y[k]] == 0:
            count += 1

paper = [[0] * 102 for i in range(102)]
count = 0
paper_count = int(input())
for i in range(paper_count):
    x, y = map(int, sys.stdin.readline().split())
    for j in range(y+1, y + 11):
        for k in range(x+1, x + 11):
            paper[j][k] = 1

for i in range(102):
    for j in range(102):
        if paper[i][j] == 1:
            checkRound(i,j,paper)

print(count)