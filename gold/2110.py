# 인자를 두개 받아서 left <= right일 때 까지 재귀? 아니다
# 그냥 공유기간 최대 가능 거리를 분할의 기준으로 삼는 것이다.
import sys
n, c = map(int, input().split())
houses = list(int(sys.stdin.readline()) for _ in range(n))
houses.sort()
d = 0
left, right = 1, houses[n-1] - houses[0]
if c == 2:
    print(houses[n-1] - houses[0])
else:
    while(left < right):
        dist = (left + right) // 2
        wifi = 1
        tmp = houses[0] # 첫 집 좌표
        for house in houses:
            if house - tmp >= dist: # 최대 가능 거리(dist = mid)보다 집사이 거리 크거나 같으면 공유기 설치
                wifi += 1
                tmp = house # 공유기를 설치할 때 마다 현재 집좌표 초기화
        
        if wifi >= c: # 공유기를 더 설치했으면 dist( = mid)값 늘려보기
            d = dist
            left = dist + 1
        elif wifi < c: # 공유기를 덜 설치했으면 dist( = mid)값 줄이기
            right = dist
        
    print(d)