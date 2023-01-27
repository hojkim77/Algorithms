N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))
dif = []
sum = 0

for i in range(len(arr) - 1):
    dif.append(arr[i + 1] - arr[i])
dif.sort()

for i in range(len(dif) - K + 1):
    sum += dif[i]
    
print(sum)