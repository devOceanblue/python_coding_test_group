"""
https://programmers.co.kr/learn/courses/30/lessons/43236
"""
# distance을 기준으로 체크
def decide(rocks,t,n):
    current = 0
    cnt = 0
    for i,rock in enumerate(rocks):
        if rock-current < t:
            if i == len(rocks):
                cnt+=1
                break
            cnt+=1
        else:
            current = rock
    return cnt > n

def solution(distance, rocks, n):
    lo = 0
    hi = distance
    rocks.sort()
    rocks.append(distance)
    
    # lower bound
    while lo<=hi:
        m = (lo+hi)//2
        if decide(rocks,m,n):
            hi = m - 1
        else:
            lo = m + 1
    
    
    return hi