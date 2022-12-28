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
        if i > 0:
            if routes[i][0] > routes[i - 1][1]:
                if flag == 1:
                    answer += 1
                flag = 1
    return answer    

print(solution([[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]))