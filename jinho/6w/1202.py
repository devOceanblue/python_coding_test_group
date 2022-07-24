"""
https://www.acmicpc.net/problem/1202

최대 가치를 얻으면 됨

아이디어
각 가방의 무게보다 작은 보석들 중 가장 가치가 큰 것을 고르자!


1. 가방을 무게를 기준으로 오름차순 정렬
2. 보석 또한 무게를 기준으로 오름차순 정렬

3. 해당 보석이 가방의 무게보다 작은 경우 maxheap에 넣기
4. 만약 가방의 무게보다 큰 보석을 만날 경우 maxheap에서 pop 한 후 더하기


왜 힙을 써야하나요?
힙의 장점중 하나인 push와 pop이 모두 logN

"""
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewerly = []
bags = []
for _ in range(N):
    M, V = map(int, input().split())
    jewerly.append((M, V))


for _ in range(K):
    bags.append(int(input()))

# 1
bags.sort()
result = 0
# 2
jewerly.sort()
max_value = []  # 가치가 큰 것들
idx = 0
for bag in bags:
    while idx < len(jewerly):
        m, v = jewerly[idx]
        # 3
        if bag >= m:
            heapq.heappush(max_value, -v)  # max_heap
            idx += 1
        else:
            break
    if max_value:
        # 4
        result += -1 * heapq.heappop(max_value)

print(result)
