import sys
input = sys.stdin.readline

def binary_search(n):
    s = 0
    e = N - 1
    while s <= e:
        m = (s + e) //2
        if N_list[m] == n:
            return 1
        elif N_list[m] > n: e = m - 1
        else: s = m + 1
    return 0

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int, input().split()))

for item in M_list:
    print(binary_search(item))

