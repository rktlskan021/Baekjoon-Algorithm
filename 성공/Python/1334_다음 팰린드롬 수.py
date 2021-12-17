
# s = int(input())
# s +=1
# s = list(map(int,list(str(s))))
#
# # 적당히 10000번쯤 돌리면 수렴함
# while True:
# # 리스트의 절반만 탐색하면 됨(어차피 앞 뒤로 같이 탐색함)
#     for i in range(0,len(s)//2+1):
#         # 앞뒤 숫자가 다른데, 뒤의 숫자가 큰 경우는 뒷의 숫자 앞의 수의 변조가 필요함.
#         if s[i] < s[len(s)-i-1]:
#             s[len(s)-i-2] += 1
#         # 그리고나서 뒤의 숫자를 앞의 숫자와 같게 만듬.
#         s[len(s)-i-1] = s[i]
#         # 자릿수 올림이 필요한 경우가 있을 수 있으니 수치를 다듬음.
#         for i in range(len(s)-1,-1,-1):
#             if s[i] >=10:
#                 s[i],s[i-1] = s[i]%10,s[i-1]+s[i]//10
#     if check(s):
#         break
# # 출력
# for i in s:
#     print(i,end="")

def check(list):
    for j in range(len(list) // 2 + 1):
        if list[j] != list[-1 - j]:
            return False
    else:
        return True

N = int(input())
N += 1
N = list(map(int,list(str(N))))

while True:
    for i in range(0,len(N)//2+1):
        if N[i] < N[-1-i]:
            N[-2-i] += 1

        N[-1-i] = N[i]

        for i in range(len(N)-1, -1, -1):
            if N[i] >= 10:
                N[i], N[i - 1] = N[i] % 10, N[i - 1] + N[i] // 10
    if check(N):
        break

for i in N:
    print(i,end="")

