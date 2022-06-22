import heapq
import sys

input = sys.stdin.readline
def soulution():
    heap = []
    for _ in range(int(input())):
        n = int(input())
        if n == 0:
            if heap: return heapq.heappop(heap)[1]
            else: return 0
        else:
            heapq.heappush(heap, (-n, n))

print(soulution())