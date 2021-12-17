if __name__ == "__main__":
    c = int(input())
    result = []
    for i in range(c):
        n, *s = map(int, input().split())
        aver = sum(s) / n
        count = 0
        for j in s:
            if aver < j:
                count += 1
        result.append(count/n*100)

    for i in result:
        print(f"{i:.3f}%")