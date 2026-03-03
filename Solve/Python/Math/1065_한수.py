if __name__ == "__main__":
    x = int(input())
    n = 0
    for i in range(1, x+1):
        if i <= 99:
            n+=1
        elif i<=999:
            i = str(i)
            if (2*int(i[1])) == int(i[0]) + int(i[2]):
                n+=1
    print(n)