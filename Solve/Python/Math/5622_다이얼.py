if __name__ == "__main__":
    number_dic = {2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}

    s = input()
    sum = 0
    for i in s:
        for j in number_dic.items():
            if i in j[1]:
                sum += (j[0]+1)
    print(sum)