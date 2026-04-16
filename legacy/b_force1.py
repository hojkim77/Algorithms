def solution(answers):
    answer = []
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans1= 0
    ans2= 0
    ans3= 0
    for i in range(len(answers)):
        if (arr1[i % len(arr1)] == answers[i % len(answers)]):
            ans1 += 1
    for i in range(len(answers)):
        print(i % len(arr2), i % len(answers))
        if (arr2[i % len(arr2)] == answers[i % len(answers)]):
            ans2 += 1
    for i in range(len(answers)):
        if (arr3[i % len(arr3)] == answers[i % len(answers)]):
            ans3 += 1
    print(ans1, ans2, ans3)
    ans = [ans1, ans2, ans3]
    for i in range(len(ans)):
        if ans[i] == max(ans):
            answer.append(i + 1)
    return answer
print(solution([1,2, 3, 4, 5]))