"""
https://www.acmicpc.net/problem/2042
"""
import sys
input = sys.stdin.readline
def calc(left,right):
    return left+right

def init(node,start,end):
    if start == end :
        segments[node] = arr[start]
        return segments[node]

    mid = (start+end)//2
    left = init(node*2,start,mid)
    right = init(node*2+1,mid+1,end)
    segments[node] = calc(left, right)
    return segments[node]

def update(idx,new_value,node,node_l,node_r): #(인덱스,update값,현재 노드,왼쪽노드,오른쪽 노드)
    if (idx <node_l) or (idx > node_r) :
        return segments[node] # default 0
    if node_l == node_r:
        segments[node] = new_value
        return segments[node]
    mid = (node_l+node_r)//2
    left = update(idx, new_value, 2*node, node_l, mid)
    right = update(idx, new_value, 2*node + 1, mid+1, node_r)
    segments[node] = calc(left, right)
    return segments[node]

def query(start,end,node,node_l,node_r): #(쿼리start,쿼리end,현재 노드,왼쪽노드,오른쪽 노드)
    if (end < node_l) or (start > node_r) :
        return 0 
    if start <= node_l and node_r <= end:
        return segments[node]

    mid = (node_l+node_r)//2
    left = query(start, end, 2*node, node_l, mid)
    right = query(start, end, 2*node+1, mid+1, node_r)
    return calc(left,right)


n,m,k = map(int,input().split())
segments = [0]*n*4
arr = []
for _ in range(n):
    arr.append(int(input()))
init(1,0,n-1)


for _ in range(m+k):
    c , a, b = map(int,input().split())
    if c == 1:
        update(a, b, 1, 0, n-1)
    elif c == 2:
        print(query(a, b, 1, 0, n-1))