def solution(number, k):
    answer = []
    for num in number:
        while answer and k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)    
    
    return ''.join(answer[:len(number) - k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))