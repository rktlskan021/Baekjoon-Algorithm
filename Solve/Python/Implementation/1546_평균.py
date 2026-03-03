if __name__ == "__main__":
    N = int(input())
    n = list(map(int, input().split()))
    Max = max(n)
    for i in range(len(n)):
        n[i] = n[i] * 100 / Max
    print(sum(n) / N)