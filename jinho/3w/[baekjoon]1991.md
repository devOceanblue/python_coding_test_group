https://www.acmicpc.net/problem/1991


## preorder
`root` -> `left` -> `right`
<img src='https://upload.wikimedia.org/wikipedia/commons/a/ac/Preorder-traversal.gif'>

## inorder
`left`->`root`->`right`
<img src='https://upload.wikimedia.org/wikipedia/commons/4/48/Inorder-traversal.gif'>

## postorder
`left`->`right`->`root`
<img src = 'https://upload.wikimedia.org/wikipedia/commons/2/28/Postorder-traversal.gif'>



## 전체코드

``` python
import sys

input = sys.stdin.readline


n = int(input())
A_start = ord('A')
trees  ={}
for _ in range(n):
    root,left,right = input().split()
    trees[root] = (left,right)

def preorder(node):
    left,right = trees[node]
    print(node,end= '')
    if left != '.':
        preorder(left)
    if right !='.':
        preorder(right)

def inorder(node):
    left,right = trees[node]
    if left != '.':
        inorder(left)
    print(node,end= '')
    if right !='.':
        inorder(right)

def postorder(node):
    left,right = trees[node]
    if left != '.':
        postorder(left)
    if right !='.':
        postorder(right)
    print(node,end= '')

functions = [preorder,inorder,postorder]

for function in functions:
    function('A')
    print()

```

