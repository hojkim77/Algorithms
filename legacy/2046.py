N = int(input())
ips = [list(map(int, input().split("."))) for _ in range(N)] 
ip = [0,0,0,0]
masked_ip = [0,0,0,0]
for i in range(32):
    cur = ips[0][i // 8] & (1 << (7 - (i % 8))) # 0번째 ip를 기준으로 나머지도 똑같은지 비교하기 위해
    for j in range(1, N):
        if cur != ips[j][i // 8] & (1 << (7 - (i % 8))): # 해당 i에 맞게 네트워크 주소, 네트워크 마스크 출력
            for x in range(4):
                if x == 3:
                    print(ip[x])
                else:
                    print(ip[x], end = ".")
            for x in range(4):
                if x == 3:
                    print(masked_ip[x])
                else:
                    print(masked_ip[x], end = ".")
            exit()
    ip[i // 8] += cur
    masked_ip[i//8] += 2 ** (7 - (i % 8)) * 1 
            
            