expression = input()

minus = expression.split("-")

l = []
for i in minus:
    plus = i.split("+")
    s = 0
    if len(plus) > 1:
        for j in plus:
            s += int(j)
        
        l.append(s)
    else:
        l.append(int(plus[0]))
    
if len(l) == 1:
    print(l[0])
else:
    s = l[0]
    for i in range(1, len(l)):
        s -= l[i]

    print(s)