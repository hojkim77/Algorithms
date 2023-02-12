# 1ver
import sys

k, n = map(int, input().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]
left, right = 1, max(lines) + 1
max_len = 0
while(left <= right):
    mid = (left + right) // 2
    answer = sum(i//mid for i in lines)
    if answer >= n:
        max_len = mid
        left = mid + 1
    elif answer < n:
        right = mid - 1
        
print(max_len)

# 2ver
import sys

k, n = map(int, input().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]
left, right = 1, max(lines) + 1

while(left < right):
    mid = (left + right) // 2
    answer = sum(i//mid for i in lines)
    if answer >= n:
        left = mid + 1
    elif answer < n:
        right = mid
        
while sum(i//mid for i in lines) >= n:
    mid += 1

print(mid -1)