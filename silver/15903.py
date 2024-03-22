import heapq

n, m = map(int, input().split())
hq = list(map(int, input().split()))
heapq.heapify(hq)

for _ in range(m):
    x, y = heapq.heappop(hq), heapq.heappop(hq)
    sumCard = x + y
    heapq.heappush(hq, sumCard)
    heapq.heappush(hq, sumCard)

print(sum(hq))
