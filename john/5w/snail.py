def solution(rounds, horizontal):
    visited = [[0, 0]]
    for round in range(1,rounds):
        # round start
        if horizontal:
            # move right
            item = list(visited[-1])
            item[1] += 1
            visited.append(item)
        else:
            # move bottom
            item = list(visited[-1])
            item[0] += 1
            visited.append(item)
        
        for move in range(round*2):
            if horizontal:
                if round > move:
                    # move bottom
                    item = list(visited[-1])
                    item[0] += 1
                    visited.append(item)
                else:
                    # move left
                    item = list(visited[-1])
                    item[1] -= 1
                    visited.append(item)
            else:
                if round > move:
                    # move right
                    item = list(visited[-1])
                    item[1] += 1
                    visited.append(item)
                else:
                    # move up
                    item = list(visited[-1])
                    item[0] -= 1
                    visited.append(item)
        horizontal = 0 if horizontal else 1
    return visited


print(solution(4,1))