S = input()
arr = []
for i in range(len(S)) :
    arr.append(S[i::])
arr.sort(reverse=False)
for i in range(len(arr)) :
    print(arr[i])