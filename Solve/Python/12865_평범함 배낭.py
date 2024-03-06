import sys

N, K = map(int, sys.stdin.readline().split())
item = [] # (무게, 가치) [(6, 13), (4, 8), (3, 6), (5, 12)]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    item.append((W,V))

M = [[0] * (K+1) for i in range(N+1)]

for i in range(1, len(M)): # i : 보석의 개수
    for j in range(len(M[i])):
        if item[i-1][0] <= j:
            if item[i-1][1] + M[i-1][j-item[i-1][0]] > M[i-1][j]:
                M[i][j] = item[i-1][1] + M[i-1][j-item[i-1][0]]
            else:
                M[i][j] = M[i-1][j]
        else:
            M[i][j] = M[i-1][j]

print(M[N][K])