if __name__ == "__main__":
    a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    alpha = input()
    for t in a:
        alpha = alpha.replace(t, '*')
    print(len(alpha))