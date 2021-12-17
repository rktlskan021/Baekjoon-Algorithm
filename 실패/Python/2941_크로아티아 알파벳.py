if __name__ == "__main__":
    List = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    front_list = ['c','d','l','n','s','z']
    s = input()
    index = 0
    tmp = ""
    result = 0
    # while True:
    #     tmp += s[index]
    #     index += 1
    #     if tmp[0] not in front_list:
    #         result += 1
    #         tmp = ""
    #         continue
    #
    #     if tmp[0] != 'd' and index == 2:
    #         if tmp in List:
    #             result += 1
    #             tmp = ""
    #             continue
    #         else:
    #             result += 1
    #             tmp = tmp[-1:]
    print(s)
    print(s[::-1])