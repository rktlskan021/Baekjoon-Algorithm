if __name__ == "__main__":
    n = int(input())
    OX = [input() for i in range(n)]

    for i in OX:
        score = 0
        check = 1
        for j in i:
            if j == 'O':
                score += check
                check += 1
            else:
                check = 1
        print(score)