def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = set([costs[0][0]])

    while len(visited) != n:
        for cost in costs:
            if cost[0] in visited and cost[1] in visited:
                continue
            if cost[0] in visited or cost[1] in visited:
                visited.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer


if __name__ == "__main__":
    assert solution(2, [[0, 1, 1]]) == 1
