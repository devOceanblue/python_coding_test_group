"""
https://www.acmicpc.net/problem/2263
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200001)

n = int(input())
inorders = list(map(int,input().split()))
postorders = list(map(int,input().split()))
results = []
inorder_idx = [0 for i in range(n+1)]
for idx,number in enumerate(inorders):
    inorder_idx[number] = idx

def get_preorder(start,end,depth):
    """
    inorder을 이용하여 postorder 구하기
    postorder을 이용하여 root 찾기
    """
    root = postorders[end-depth]
    idx = inorder_idx[root]
    if start  == end:
        results.append(inorders[end])
        return 
    elif start < end  < n:
        # root 
        results.append(root)
        # left 
        get_preorder(start, idx-1,depth)
        # right
        get_preorder(idx+1, end,depth+1)
        return 


get_preorder(0, n-1,0)
print(*results)
"""
inorder : left -> root -> right
postorder : left -> right -> root
preorder : root -> left -> right

inputs
7
4 2 5 1 6 3 7
4 5 2 6 7 3 1

15
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
"""