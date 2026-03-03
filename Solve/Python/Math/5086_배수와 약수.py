import sys
input = sys.stdin.readline

def discrimination(a, b):
	if a>b:
		if a % b == 0:
			return "multiple"
	else:
		if b % a == 0:
			return "factor"
	return "neither"
		

while True:
	a, b = map(int, input().split())
	if a == b:
		break
	print(discrimination(a, b))
