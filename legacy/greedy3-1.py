def solution(number, k):
    answer = ""
    arr = list(number)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    
    min_num = 0
    while(k > 0):
        find = False
        for i in range(len(arr) - 1):
            if (arr[i] == min_num and find == False):
                arr.pop(i)
                k -= 1
                find = True
        if (find == False):
            min_num += 1
    return "".join(map(str,arr))


print(solution("4177255555", 4))