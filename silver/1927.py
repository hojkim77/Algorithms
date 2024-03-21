# heapq
import sys
import heapq

input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    i = int(input())
    if i == 0:
        if h == []:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, i)
