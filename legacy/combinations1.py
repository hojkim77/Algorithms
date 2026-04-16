# 후보키
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    answer = []
    for n in range(1, col + 1):
        for c in combinations(range(col), n):
            tmp = [tuple(item[key] for key in c) for item in relation]
            if len(set(tmp)) == row:
                flag = False
                for i in answer:
                    if len(set(i)) == len(set(c) & set(i)):
                        flag = True
                        break
                            
                if not flag:
                    answer.append(c)
                
    return len(answer)