import sys
import math
input = sys.stdin.readline
n = int(input())

distance = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
m = math.inf
for i in range(0, n-1):
    if prices[i] < m:
        m = prices[i]
    result += m * distance[i]

print(result)

'''
지금 당장 최선의 선택을 한다.
우선 첫번째 도시에서 무조건 기름을 사야함. -> 얼만큼 사야 하는가? -> 최소 다음 도시 or 마지막 도시까지 가는 만큼

가장 싼 도시에서 끝까지 가는 기름을 삼.
'''