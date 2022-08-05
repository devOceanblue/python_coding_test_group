import heapq


def solution(operations):
    queue = []
    for operation in operations:
        op, num = operation.split(" ")
        num = int(num)
        if op == "I":
            heapq.heappush(queue, num)
        else:
            if not queue:
                continue
            if num == -1:
                minimum = heapq.nsmallest(1, queue)[0]
                queue.remove(minimum)
            else:
                maximum = heapq.nlargest(1, queue)[0]
                queue.remove(maximum)
    if not queue:
        return [0, 0]
    else:
        return [heapq.nlargest(1, queue)[0], heapq.nsmallest(1, queue)[0]]


if __name__ == "__main__":
    print(
        solution(
            ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
        )
    )
