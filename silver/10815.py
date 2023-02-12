N = int(input())
narr = list(map(int, input().split()))
narr.sort()
M = int(input())
marr = list(map(int, input().split()))

for m in marr:
    left, right = 0, N
    while(left < right):
        mid = (left + right) // 2
        if narr[mid] > m:
            right = mid
        elif narr[mid] < m:
            left = mid + 1
        else:
            print(1)
            break
    if left >= right:
        print(0)
