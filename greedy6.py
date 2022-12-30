from collections import deque

def solution(routes):
    answer = 0
    routes.sort()
    print(routes)
    end = -30000
    flag = 0
    
    for i in range(len(routes)):
        if routes[i][0] > end:
            end = routes[i][1]
            print(end)
            answer += 1
            flag = 0
        
        elif routes[i][0] <= end:  
            if i > 0:
                if routes[i][0] > routes[i - 1][1] and routes[i][1] < end:
                    if flag == 1:
                        answer += 1
                    flag = 1
    return answer    

print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]]))