import sys
input = sys.stdin.readline
n = int(input())

sequence = [0] * n
for i in range(n):
    sequence[i] = int(input())

result = 0
positive = []
negative = []
zero = False

for num in sequence:
    if num > 1:
        positive.append(num)
    elif num == 1:
        result += 1
    elif num == 0:
        zero = True
    else:
        negative.append(num)

tmp = []
positive.sort(reverse=True)
for num in positive:
    tmp.append(num)
    if len(tmp) == 2: 
        result += tmp[0] * tmp[1]
        tmp.clear()

if tmp: 
    result += tmp[0]
    tmp.clear()

negative.sort()
for num in negative:
    tmp.append(num)
    if len(tmp) == 2:
        result += tmp[0] * tmp[1]
        tmp.clear()

if tmp:
    if not zero:
        result += tmp[0]

print(result)

'''
1. 0이 있다면 양수와 묶지 말고, 음수 중 가장 큰 값과 묶기
2. 1이 있을 때는 곱해도 의미가 없기 때문에 그냥 더하기
3. 양수는 2 이상인 값만 묶기
4. 음수끼리 곱하면 양수... 를 까먹고 있었네
'''