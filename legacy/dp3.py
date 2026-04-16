n = int(input())

d = [0] * (n + 1)

def make_tile(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    
    if d[x] != 0:
        return d[x]
    d[x] = 2 * make_tile(x - 2) + make_tile(x - 1)
    
    return d[x]

print(make_tile(n) % 10007)