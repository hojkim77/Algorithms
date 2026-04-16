def solution(citations):
    answer = 0
    sorted_arr = sorted(citations, reverse=True)
    for i in range(len(sorted_arr)):
        if sorted_arr[i] <= i + 1:
            answer = sorted_arr[i]
            if answer < i:
                answer = i
            return answer
    return len(citations)
print(solution([4,4,4]))