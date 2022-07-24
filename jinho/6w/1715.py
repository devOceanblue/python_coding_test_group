"""
https://www.acmicpc.net/problem/1715

아이디어

카드의 수가 많은 것을 먼저 섞을 경우 연산 수가 매우 많아짐

ex) 10, 20 ,30 ,40
(10+20) + (30+30) + (60+40) => 190
   A       A +30       B +40
             = B

ex) 40, 30 , 20, 10
(40+30) + (70+20) +(90+ 10) => 260
   A'        A'+20   B`+10
             = B'
따라서 카드를 minheapify 하고
가장 작은 2개를 빼서 더한 값을 다시 넣자



1. minheap
2. 연산 횟수
3. 다시 힙에 넣기

"""

import sys
import heapq

input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

min_heap = []
# 1
for num in arr:
    heapq.heappush(min_heap, num)

result = 0
while len(min_heap) > 1:
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)
    # 2
    result += a + b
    # 3
    heapq.heappush(min_heap, a + b)

print(result)
