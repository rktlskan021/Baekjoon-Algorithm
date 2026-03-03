if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        r, s = input().split()
        r = int(r)
        for j in s:
            print(j * r, end="")
        print()
