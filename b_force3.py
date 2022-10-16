def solution(brown, yellow):
    answer = []
    border = (brown - 4) // 2
    
    for i in range(border):
        if i * (border - i) == yellow:
            if i + 2 not in answer:
                answer.append(i+ 2)
            if border - i + 2 not in answer:   
                answer.append(border - i + 2)
    if (len(answer) == 1):
        answer.append(answer[0])
    answer.sort(reverse=True)
    return answer