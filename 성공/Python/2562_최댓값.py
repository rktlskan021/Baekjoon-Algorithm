if __name__ == "__main__":
    List = []
    for i in range(9):
        List.append(int(input()))

    Max = max(List)
    print(Max)
    print(List.index(Max) + 1)
