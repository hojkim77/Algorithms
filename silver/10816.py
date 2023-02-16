N = int(input())
arr = list(map(int, input().split()))
arr.sort()
narr = []
for i in arr:
    if narr:
        if narr[len(narr) - 1][0] == i:
            narr[len(narr) - 1][1] += 1
        else:
            narr.append([i, 1])
    else:
        narr.append([i, 1])
M = int(input())
marr = list(map(int, input().split()))

for m in marr:
    left, right = 0, len(narr)
    flag = False
    while(left < right):
        mid = (left + right) // 2
        if narr[mid][0] > m:
            right = mid
        elif narr[mid][0] < m:
            left = mid + 1
        else:
            print(narr[mid][1])
            flag =True
            break
    if flag == False:
        print(0)
