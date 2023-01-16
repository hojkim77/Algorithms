arr = [list(map(int, input().split())) for _ in range(19)]
dxy = ((1,1), (0, 1), (1, 0), (1, -1))

def check(i, j, n): ## ver.2
    #print('s ', i, j)
    for d in dxy:
        cnt = 1
        x, y = j + d[1], i + d[0]
        while 0<=x<19 and 0<=y<19 and arr[y][x] == n:
            #print('cnt ', cnt)
            cnt += 1
            x += d[1]
            y += d[0]
            if cnt == 5:
                if (0<=x<19 and 0<=y<19 and arr[y][x] == n):
                    break
                if (0<=i - d[0]<19 and 0<=j - d[1]<19 and arr[i - d[0]][j - d[1]] == n):
                        break
                else:
                    print(i + 1, j + 1)
                    if d == (1, -1):
                        print(arr[i][j])
                        print(i + 5, j - 3)
                    else:
                        print(arr[i][j])
                        print(i + 1, j + 1)
                    exit()

                    
def solution():
    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                check(i, j, arr[i][j])
                    
    print(0)

solution()


''' ver.1
def check1(i, j, n):
    if arr[i - 1][j + 1] == n:
        return 6
    for _ in range(4):
        i += 1
        j -= 1
        if 0 < i < 19 and 0 < j < 19:
            if arr[i][j] != n:
                return False
        else:
            return False
    if 0 < i - 1 < 19 and 0 < j + 1 < 19:
        if arr[i + 1][j - 1] != n:
            return True
        else:
            return 6
def check2(i, j, n):
    if arr[i][j - 1] == n:
        return 6
    for _ in range(4):
        j += 1
        if 0 < i < 19 and 0 < j < 19:
            if arr[i][j] != n:
                return False
        else:
            return False
    if 0 < i < 19 and 0 < j + 1 < 19:
        if arr[i][j + 1] != n:
            return True
        else:
            return 6 
def check3(i, j, n):
    if arr[i - 1][j - 1] == n:
        return 6
    for _ in range(4):
        i += 1
        j += 1
        if 0 < i < 19 and 0 < j < 19:
            if arr[i][j] != n:
                return False
        else:
            return False
    if 0 < i + 1 < 19 and 0 < j + 1 < 19:
        if arr[i + 1][j + 1] != n:
            return True
        else:
            return 6
def check4(i, j, n):
    if arr[i - 1][j] == n:
        return 6
    for _ in range(4):
        i += 1
        if 0 < i < 19 and 0 < j < 19:
            if arr[i][j] != n:
                return False
        else:
            return False
    if 0 < i + 1 < 19 and 0 < j < 19:
        if arr[i + 1][j] != n:
            return True
        else:
            return 6
'''