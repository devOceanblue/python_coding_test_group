"""
https://www.acmicpc.net/problem/1920
"""

import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
targets = list(map(int,input().split()))


numbers.sort()

for t in targets:
    s,e = 0,N-1
    while s<=e:
        m = (s+e)//2
        if numbers[m] == t:
            print(1)
            break
        elif numbers[m] < t:
            s = m+1
        else:
            e = m-1
    else:
        print(0)