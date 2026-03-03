def d(n):
    Sum = n
    n = str(n)
    for i in n:
        Sum += int(i)
    return Sum

if __name__ == "__main__":
    List = []
    for i in range(1, 10001):
        List.append(d(i))

    for i in range(1,10001):
        if i not in List:
            print(i)