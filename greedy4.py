def solution(people, limit):
    answer = 0
    f_min = 0
    people.sort()
    while(len(people) > 0):
        if (len(people) == 1):
            answer += 1
            return answer
        f_min = people.pop(0)
        for i in reversed(range(len(people) - 1)):
            if (f_min + people[i] <= limit):
                people.pop(i)
                break
        answer += 1
    return answer
##pop사용시 효율성 문제




print(solution([100,500,500,900,950], 1000))