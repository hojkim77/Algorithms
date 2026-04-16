n = int(input())


def make_num(x):
    num = [0] * (x + 1)

    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    num[1] = 1
    num[2] = 2
    num[3] = 4

    for i in range(x + 1):
        if i > 3:
            num[i] = num[i - 1] + num[i - 2] + num[i - 3]
    #if d[x] != 0:
    #    return d[x]
    #d[x] = make_num(n - 3) +  make_num(x - 2) + make_num(x - 1)
    
    return num[x]

for i in range(n):
    a = int(input())
    print(make_num(a))
