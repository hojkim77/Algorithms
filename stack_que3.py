from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck = deque(truck_weights) # truck queue 생성
    going = [0] * (bridge_length) # 가는중인 트럭 초기화
    going[bridge_length - 1] = truck.popleft() # 첫 트럭 시작
    sum_weight = going[bridge_length - 1]

    while(truck):
        #print(truck)
        #print(answer)
        #print(going)
        answer += 1
        sum_weight -= going[0]
        for i in range(1, bridge_length): # 트럭 한 칸씩 앞당기
            going[i - 1] = going[i]
        going[bridge_length - 1] = 0
        
        if (sum_weight + truck[0] <= weight):
            sum_weight += truck[0]
            going[bridge_length - 1] = truck.popleft()
    answer += bridge_length
    return answer
print(solution(2,10,[7,4,5,6]))