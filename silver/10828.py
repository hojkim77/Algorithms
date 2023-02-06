import sys
arr = []
def stack(methods, x):
    global arr
    if methods == "push":
        arr.append(x)
    elif methods == "pop":
        if not len(arr):
            return -1
        else:
            return(arr.pop(len(arr) - 1))
    elif methods == "size":
        return(len(arr))
    elif methods == "empty":
        if (len(arr)):
            return 0
        else:
            return 1
    elif methods == "top":
        if not (len(arr)):
            return -1
        else:
            return arr[len(arr) - 1]
        
N = int(sys.stdin.readline())
for _ in range(N):
    input = list(sys.stdin.readline().split())
    if len(input) == 1:
        print(stack(input[0], 0))
    elif len(input) == 2:
        stack(input[0],int(input[1]))
