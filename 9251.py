if __name__ == "__main__":
    first = input()
    second = input()
    i = 0
    j = 0
    answer = 0
    while True:
        if i == len(first) - 1 or j == len(second) - 1:
            break
        for jj in range(j, len(second)):
            if first[i] == second[jj]:
                answer += 1
                j = jj
                break
        i += 1
    print(answer)
    #
    # ACAYKP
    # CAPAKC