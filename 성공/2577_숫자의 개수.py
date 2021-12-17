if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    mult = str(a*b*c)
    for i in range(10):
        print(mult.count(str(i)))
