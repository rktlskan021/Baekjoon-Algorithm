if __name__ == "__main__":
    s = input()
    dic = {}
    for i in s:
        if i.upper() in dic:
            dic[i.upper()] += 1
        else:
            dic[i.upper()] = 1

    m = max(dic.values())
    if list(dic.values()).count(m) >= 2:
        print("?")
    else:
        for i in dic.items():
            if i[1] == m:
                print(i[0])
