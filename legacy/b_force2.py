from itertools import combinations, permutations

def is_prime(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def string_to_num(arr):
    num = 0
    for i in range(len(arr), 0, -1):
        num += int(arr[i - 1]) * (10**(len(arr) - i))
    return num

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        arr = list(permutations(list((numbers)), i + 1))
        for i in range(len(arr)):#3중 for 문 써야할듯
            if (is_prime(string_to_num(arr[i]))):
                if string_to_num(arr[i]) not in answer and string_to_num(arr[i]) != 0 and string_to_num(arr[i]) != 1:
                    answer.append(string_to_num(arr[i]))
    print(answer)
    return len(answer)

print(solution("1231"))