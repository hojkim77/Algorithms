n = int(input())
arr = [list(str(input())) for _ in range(n)]
answer = ""

def quad(n, x, y):
    global answer
    if n == 1:
        answer += arr[x][y]
    else:  
        sum = 0
        for i in range(n):
            for j in range(n):
                sum += int(arr[x + i][y + j])
        if sum == 0:
            answer += '0'
        elif sum == (n) *(n):
            answer += '1'
        else:
            answer += "("
            quad(n // 2, x, y)
            quad(n // 2, x, y + n // 2)
            quad(n // 2, x + n // 2, y)
            quad(n // 2, x + n // 2, y + n // 2)
            answer += ")"
            
quad(n, 0, 0)

print(answer)
