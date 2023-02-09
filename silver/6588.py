import math
from sys import stdin

prime_arr = [1] * 1000001
prime_arr[0], prime_arr[1] = 0, 0
for i in range(2, int(math.sqrt(1000000)) + 1):
    if prime_arr[i] == 1:
        for j in range(i + i, 1000001, i):
            prime_arr[j] = 0
# 에라토스테네스의 체
# 어떠한 숫자 n에 대하여 그의 배수들은 모두 소수가 아니라는 개념.

while(True):
    N = int(stdin.readline())
    if N == 0:
        exit()
    i = 2
    while(i <= N // 2 + 1):
        if prime_arr[i] == 1 and prime_arr[N - i] == 1:
            print(N, '=',i, '+',N - i ) 
            break
        i += 1

    if i > N // 2:
        print("Goldbach's conjecture is wrong.")