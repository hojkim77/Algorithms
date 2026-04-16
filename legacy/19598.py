import heapq

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])

rooms = []
for room in arr:
    heapq.heappush(rooms,room[1])
    if rooms and rooms[0] <= room[0]:
        heapq.heappop(rooms)

print(len(rooms))

# 시작 시간대로 정렬을 했으니 끝나는 시간은 어떻게 되는지 모르니까 힙구조를 쓰는거구나.

# 회의가 끝나는 시간과 가장 가까운 시작시간을 가진 회의와 이어져야한다.

# 회의 시작시간대로 정렬을 하면, 결국 이어지지 못하고 쌓이던 회의들이(끝나는 순서로 정렬됨) 가장 자신과 가까운 회의를 만나 없어지게됨.
