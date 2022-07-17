n = int(input())
array = sorted(list(map(int, input().split())))
print(sum([sum(array[:i + 1]) for i in range(n)]) )