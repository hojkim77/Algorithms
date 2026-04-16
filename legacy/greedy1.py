def solution(n, lost, reserve):
    answer = 0
    arr = []
    for i in range(n):
        arr.append(1)
    for i in lost :
        arr[i - 1] -= 1
    print(arr)
    for i in reserve:
        arr[i - 1] += 1
    print(arr)

    for i in reserve:
        if arr[i - 1] > 1:    
            if i == 1: # 0
                if arr[0] > 1:
                    if arr[1] < 1:
                        arr[1] += 1
                elif arr[0] < 1:
                    arr[0] += 1
            elif i == n: # n
                if arr[i - 1] > 1:
                    if arr[i - 2] < 1:
                        arr[i - 2] += 1
                elif arr[i - 1] < 1:
                    arr[i - 1] += 1
                    
            elif arr[i - 1] > 1: #general
                if arr[i - 2] < 1:
                    arr[i - 2] += 1
                    arr[i - 1] -= 1
                elif arr[i] < 1:
                    arr[i] += 1
                    arr[i - 1] -= 1

        
    for i in arr:
        if i > 0:
            answer += 1
    return answer

print(solution(5, [4,2], [3,5]))