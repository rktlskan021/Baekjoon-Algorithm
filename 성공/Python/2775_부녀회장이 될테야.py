# 1
T = int(input())
for _ in range(T):
	k = int(input())
	n = int(input())
	apt = [i for i in range(1, n+1)]
	for i in range(k):
		tmp = []
		for j in range(n):
			tmp.append(sum(apt[:j+1]))
		apt = tmp
	print(apt[-1])	
  
# 2
def sum(arr):
	j = 0
	for i in arr:
		j += i
	return j

apt = [[0 for _ in range(14)] for __ in range(15)]
for k in range(15):
	for n in range(14):
		if k == 0:
			apt[k][n] = n+1
			continue
		apt[k][n] = sum(apt[k-1][:n+1])
			
T = int(input())
for i in range(T):
	k = int(input())
	n = int(input())
	print(apt[k][n-1])
