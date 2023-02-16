E, S, M = map(int, input().split())

esm = [1,1,1]
answer = 1
while(True):
    if (E == esm[0] and S == esm[1] and M == esm[2]):
        break
    esm[0], esm[1], esm[2] = esm[0] + 1, esm[1] + 1, esm[2] + 1
    answer += 1
    if esm[0] == 16:
        esm[0] = 1
    if esm[1] == 29:
        esm[1] = 1
    if esm[2] == 20:
        esm[2] = 1
print(answer)