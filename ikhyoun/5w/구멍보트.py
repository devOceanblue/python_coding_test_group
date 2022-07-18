def solution(people, limit):
    people.sort()
    length = len(people)
    answer = 0
    start = 0
    end = length - 1
    while start < end:
        value = people[start] + people[end]
        if value > limit:
            end -= 1
        else:
            answer += 1
            start += 1
            end -= 1
            length -= 1
    answer += length - start        
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))