if __name__ == "__main__":
    a, b, v = map(int, input().split())
    day = (v-b)/(a-b)
    print(int(day) if int(day) == day else int(day) + 1)