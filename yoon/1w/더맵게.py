from heapq import heapify, heappop, heappush


def solution(scoville, K):
    count = 0
    heapify(scoville)
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            break
        if scoville[0] >= K:
            return count

        temp = []
        for i in range(2):
            temp.append(heappop(scoville))
        heappush(scoville, temp[0] + temp[1] * 2)
        count += 1
    return -1


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 5))
