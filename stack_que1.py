def solution(progresses, speeds):
    answer = []
    days = [0] * len(progresses)
    for i in range(len(progresses)):
        days[i] = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] > 0:
            days[i] += 1
    cnt = 0
    j = 0 #max index
    print(days)
    for i in range(len(days)):
        if i == 0:
            cnt += 1
        elif days[i] <= days[j]:
            cnt += 1
        else:
            j = i
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer

print(solution([90,90,90,90,90,90,90,90], [3,5,6,7,5,4,1,2]	))