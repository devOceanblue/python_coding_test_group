def solution(begin, target, words):
    def can_change(a,b):
        cnt = 0
        for x,y in zip(a,b):
            if x != y:
                cnt+=1
        if cnt == 1:
            return True
        return False
    
    
    visited = [False for _ in range(len(words))]
    
    from collections import deque
    Q =deque()
    Q.append((begin,0))
    while Q:
        current,cnt = Q.popleft()
        if current == target:
            return cnt
        if cnt == len(words):
            return 0
        
        for word in words:
            if can_change(word,current):
                Q.append((word,cnt+1))
    return 0