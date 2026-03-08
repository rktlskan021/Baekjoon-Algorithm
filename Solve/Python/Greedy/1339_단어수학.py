import sys
input = sys.stdin.readline
n = int(input())

words = []
for i in range(n):
    words.append(input().rstrip())

weight = {}
for word in words:
    for w in range(len(word)):
        if word[w] in weight:
            weight[word[w]] += 10 ** (len(word) - (w + 1))
        else:
            weight[word[w]] = 10 ** (len(word) - (w + 1))

number = 9
result = 0
for value in sorted(list(weight.values()), reverse=True):
    result += number * value
    number -= 1

print(result)

'''
단위수가 높은 것부터 높은 가중치 부여
'''