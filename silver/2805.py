n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 1, max(trees)
maxlen = 0

mintree = min(trees)
sumtree = sum(tree - mintree for tree in trees)
print(sumtree)
if sumtree == m:
    print(mintree)
else:
    if sumtree > m:
        left, right = mintree - 1, max(trees)
    elif sumtree < m:
        left, right = 1, mintree + 1
print(left, right)

while(left <= right):
    mid = (left + right) // 2
    total = 0
    for tree in trees:
        if tree - mid > 0:
            total += tree - mid
        if total > m: # 이 때를 멈춰줘야했다,,
            break
    print(total)
    if total >= m:
        maxlen = mid
        left = mid + 1
           
    elif total < m:
        right = mid - 1
        

print(maxlen)