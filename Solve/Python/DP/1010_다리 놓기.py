import sys
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    N, M = map(int, input().split())

    answer = math.factorial(M) // (math.factorial(N) * math.factorial(M-N))

    print(answer)