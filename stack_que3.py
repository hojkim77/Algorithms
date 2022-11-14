def solution(bridge_length, weight, truck_weights):
    answer = 0
    going = []
    intgoing = 0
    while(truck_weights):
        print(truck_weights)
        if(sum(going) + truck_weights[0] <= weight and len(going) < bridge_length):
            if (going):
                answer += 1
                going.append(truck_weights.pop(0))
            else:
                answer += bridge_length
                going.append(truck_weights.pop(0))
        intgoing += 1
        if (intgoing == bridge_length):
            going.pop(0)
            answer += 1
            intgoing = 0
    if(going):
        answer += len(going)
    return answer

print(solution(5,5,[2,2,2,2,1,1,1,1,1]))