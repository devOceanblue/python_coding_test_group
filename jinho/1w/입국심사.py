"""
https://programmers.co.kr/learn/courses/30/lessons/43238
"""

def solution(n, times):
    def decide(times,t):
        cnt = 0
        for time in times:
            cnt += t//time
        
        if cnt >= n:
            return True
        else:
            return False
                
    
    
    lo = 1
    hi = max(times) * n
    
    while lo<= hi:
        m = (lo+hi)//2
        if decide(times,m):
            hi = m-1
        else:
            lo = m+1
    return lo