N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split()))) # 좌표 정렬
dif = []
sum = 0

for i in range(len(arr) - 1): # 정렬된 좌표간의 차이 걔선
    dif.append(arr[i + 1] - arr[i])
dif.sort()

for i in range(len(dif) - K + 1): # 가장 큰 좌표 N - (K + 1)개 제외하고 모두 합
    sum += dif[i]
    
print(sum)