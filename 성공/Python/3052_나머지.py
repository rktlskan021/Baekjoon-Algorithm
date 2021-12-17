if __name__ == "__main__":
    List = [int(input()) for i in range(10)]
    check = []
    for i in List:
        if (i % 42) not in check:
            check.append(i % 42)

    print(len(check))
