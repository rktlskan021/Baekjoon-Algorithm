#if __name__ == "__main__":
    # 내가 푼 방식
    # N = int(input())
    # result = 0
    # check = 0
    # for i in range(N):
    #     s = input()
    #     check = 0
    #     for j in s:
    #         count = s.count(j)
    #         if count == 1:
    #             check += 1
    #             continue
    #
    #         index = s.index(j)
    #
    #         if s[index:index+count] == j*count:
    #             check += 1
    #
    #     if check == len(s):
    #         result += 1
    # print(result)

    # 또 다른 방식
    # result = 0
    # for i in range(int(input())):
    #     word = input()
    #     if list(word) == sorted(word, key=word.find):
    #         result += 1
    # print(result)