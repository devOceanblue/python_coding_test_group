def check(houses,distance):
    current = houses[0] 
    cnt = 1
    for house in houses:
        if house - current >= distance:
            cnt+=1
            current = house
    return cnt

import sys
input = sys.stdin.readline
N, C = map(int,input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
min_d,max_d = 0,houses[-1]
while min_d<=max_d:
    d = (min_d+max_d)//2
    if check(houses,d)>=C: # 공유기 개수가 같거나 많을 시 거리를 늘려야 함
        ans = d
        min_d=d+1
    else: # 공유기 개수가 작을 시 거리를 줄여야함
        max_d = d-1
print(ans)
