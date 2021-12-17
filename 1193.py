if __name__ == "__main__":
    x = int(input())
    line = 1
    plus = 1
    while plus < x:
        line += 1
        plus += line

    if line % 2 == 0:
        numerator = line
        for i in range(1, line + 1):
            denominator = i
            if plus == x:
                print(f'{numerator}/{denominator}')
                break
            else:
                plus -= 1
                numerator -= 1
    else:
        denominator = line
        for i in range(1, line + 1):
            numerator = i
            if plus == x:
                print(f'{numerator}/{denominator}')
                break
            else:
                plus -= 1
                denominator -= 1