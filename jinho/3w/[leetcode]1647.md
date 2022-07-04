https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


# Solution
문자열의 문자하나하나 체크하여 빈도수를 증가하는 딕셔너리 사용
``` python
frequencies = defaultdict(int)
for c in s:
    frequencies[c] +=1
```

이후 해당 문자와 빈도수를 최대힙에 넣음

최대힙에서 최대값(pop)한 것과 현재 남은 힙에서의 최댓값이 같을 경우  
`1`을 증가하여 push (최대힙은 부호가 반대이므로 `음수`값임)

## 전체 코드
``` python
class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import defaultdict
        import heapq
        frequencies = defaultdict(int)
        for c in s:
            frequencies[c] +=1
        cnt = 0
        Q = []
        for c in frequencies:
            heapq.heappush(Q,(-frequencies[c],c))
        
        while len(Q) > 1:
            fre, c = heapq.heappop(Q)
            if fre == Q[0][0]:
                cnt+=1
                if fre+1 !=0:
                    heapq.heappush(Q,(fre+1,c))
        
        return cnt
``` 
## 시간복잡도 
O(K^2logK) K : 다른 문자 수    
빈도수 a = 100, b= 100,c= 100,d=100 ....  
(K-1) + (K-2) + ..... 2 + 1 = O(K^2)  
heappush = O(logK)
## 결과
Runtime: `145 ms`, faster than `97.47%` of Python online submissions for Minimum Deletions to Make Character Frequencies Unique.

Memory Usage: `14.3 MB`, less than `75.11%` of Python online submissions for Minimum Deletions to Make Character Frequencies Unique.

