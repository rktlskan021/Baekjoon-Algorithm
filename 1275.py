import sys
if __name__ == "__main__":
    N, Q = map(int, sys.stdin.readline().split())
    N_list = list(map(int, sys.stdin.readline().split()))

    for i in range(Q):
        cal_list = list(map(int, sys.stdin.readline().split()))
        x = cal_list[0]
        y = cal_list[1]
        a = cal_list[2]
        b = cal_list[3]

        if x<y:
            print(sum(N_list[x-1:y]))
        else:
            print(sum(N_list[y - 1:x]))
        N_list[a-1] = b

