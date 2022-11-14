def compare(n):
    n = n*4
    return n[0:4]

def solution(numbers):
    answer = ''
    str_arr = [str(s) for s in numbers]
    sorted_arr = sorted(str_arr, key=lambda x:compare(x), reverse=True)
    for i in range(len(sorted_arr) - 1):
        if int(sorted_arr[i]) == 10 * int(sorted_arr[i + 1]):
            sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
    
    answer = ''.join(str(s) for s in sorted_arr)
    
    return str(int(answer))

print(solution([45, 454]))