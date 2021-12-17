if __name__ == "__main__":
    n = int(input())
    if n == 1:
        print(1)
        exit()
    line = 1
    count = 1
    plus = 6
    while line < n:
        line += plus
        plus += 6
        count += 1
    print(count)

# 6씩 증가