def solution(A, B):
    for item in B:
        s, e = 0, N - 1
        flag = 0
        while s <= e:
            m = (s + e) // 2
            if N_list[m] == item:
                flag = 1
                break
            elif N_list[m] > item:
                e = m - 1
            else: s = m + 1
        print(flag, end = ' ')
        

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

solution(N_list, M_list)