import sys
import heapq
input = sys.stdin.readline

array = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(array, (abs(x), x))
    else:
        if array:
            print(heapq.heappop(array)[1])
        else: print(0)