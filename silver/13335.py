# simulation

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
# 진행중인 트럭
going = [0] * w
# 진행중인 트럭 무게
weight = 0
# 흐른 시간
time = 0

while trucks:
    # 시간 추가
    time += 1
    # 트럭 한 칸 앞으로 이동
    weight -= going.pop(0)

    # 다리 하중이 버티면 트럭 추가
    if weight + trucks[0] <= L:
        goTruck = trucks.pop(0)
        going.append(goTruck)
        weight += goTruck
    # 그렇지 않으면 추가 X
    else:
        going.append(0)

# 트럭이 모두 나갔으므로, 가장 최근에 나간 트럭은 다리 끝에 있음. 따라서 다리 길이만큼 시간 추가.
time += w

print(time)
