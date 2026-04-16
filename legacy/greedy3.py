def solution1(number, k):
    arr = list(number)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    max =[arr[0]]
    num_i = 1
    if len(number) == 2:
        return max(arr)
    while (k > 0 and len(max) < len(number) - k):
        if (max[-1] > arr[num_i]):
            if num_i != len(arr) -1:
                if (arr[num_i] > arr[num_i + 1]):
                    max.append(arr[num_i])
                    num_i += 1

                else:
                    num_i += 1
                    k -= 1
            else:
                return "".join(map(str,max))

                
        elif (max[-1] < arr[num_i]):
            while max[-1] < arr[num_i] and k > 0:
                max.pop()
                k -= 1
                if not max or k <= 0:
                    break
            max.append(arr[num_i])
            num_i += 1

        else:
            max.append(arr[num_i])
            num_i += 1
    if (len(max) < len(number) - k):    
        for i in range(num_i, len(arr)):
            max.append(arr[i])
            
    return "".join(map(str,max))


print(solution1("111111", 2))



def solution2(number, k):
    answer = []

    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)

print(solution2("111111", 2))

'''def solution(number, k):
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
    return "".join(map(str,arr))'''