def solution(routes):
    count = 1
    routes.sort(key = lambda x: x[1])
    located = routes[0][1]
    for start, end in routes[1:]:
        if located < start:
            count +=1
            located = end
    return count

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))