# Z

N, r, c = map(int, input().split())

answer = 0

def Z(x, y, n):
    global answer
    print(x, y, answer)
    if (r == 0 and c == 0):
        print(0)
        exit()
        
    if n == 1:
        if x == r and y == c:
            print(answer)
        elif x == r and y + 1 == c:
            print(answer + 1)
        elif x + 1 == r and y == c:
                print(answer + 2)
        elif x + 1 == r and y + 1 == c:
            print(answer + 3)
                        
        
    else:
        if (r < x + 2 ** (n - 1) and c <  y + 2 ** (n - 1)):
            Z(x, y, n - 1)
        elif (r <  x + 2 ** (n - 1) and c >=  y + 2 ** (n - 1)):
            answer += ((2**n) // 2) ** 2 
            Z(x, y + 2 ** (n - 1), n - 1)
        elif (r >=  x + 2 ** (n - 1) and c < y + 2 ** (n - 1)):
            answer += ((2**n) // 2) ** 2 * 2
            Z(x + 2 ** (n - 1), y, n - 1)
        else:
            answer += ((2**n) // 2) ** 2 * 3
            Z(x + 2 ** (n - 1), y + 2 ** (n - 1), n - 1)
        
Z(0,0,N)