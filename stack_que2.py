def solution(priorities, location):
    answer = 0
    print(priorities)

    while(1):
        print(priorities)
        print(location)
        if priorities[0] == max(priorities):
            if location == 0:
                answer += 1
                break
            priorities.pop(0)
            location -= 1
            answer += 1
            
        elif priorities[0] < max(priorities):
            tmp = priorities.pop(0)
            priorities.append(tmp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    
    return answer

print(solution([1, 1, 9, 1, 1, 1],0))