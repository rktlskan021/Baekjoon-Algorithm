import sys
input = sys.stdin.readline

while True:
	n = int(input())
	if n == -1:
		break
	s = 0
	l = []
	for i in range(1, n):
		if n % i == 0:
			s += i
			l.append(str(i))
	if n == s:
		print("{} = ".format(n), end="")
		print(" + ".join(l))
	else:
		print(n, "is NOT perfect.")
