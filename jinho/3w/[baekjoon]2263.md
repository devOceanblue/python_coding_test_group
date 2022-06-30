# 아이디어

postorder의 경우 left -> right -> root

inorder  
<img src='https://upload.wikimedia.org/wikipedia/commons/4/48/Inorder-traversal.gif'>
postorder   
<img src = 'https://upload.wikimedia.org/wikipedia/commons/2/28/Postorder-traversal.gif'>

inorder :  left -> root -> right
| A | B | C | D | E | F | G | H | I       |
| -- | :--: | -- | -- | -- | -- | -- | -- | -- |
| left  |||||                    root   ||right|



postorder : left -> right -> root

| A | C | E | D | B | H | I | G | F       |
| -- | :--: | -- | -- | -- | -- | -- | -- | -- |
| left  |||||                    right   |||root|

# 첫 시도
``` python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inorders = list(map(int,input().split()))
postorders = list(map(int,input().split()))

inorder_idx = {}
for idx,number in enumerate(inorders):
    inorder_idx[number] = idx


def get_preorder(start,end,depth):

    root = postorders[end-depth]
    idx = inorder_idx[root]
    if start  == end:
        print(inorders[end],end=' ')
        return 
    # root 
    print(root,end=' ')
    # left 
    get_preorder(start, idx-1,depth)
    # right
    get_preorder(idx+1, end,depth+1)
    return 
```
실행 결과 : `메모리 초과` , `출력 초과`

맨 처음 메모리 초과가 난 이유가 최적화를 덜 했다고 생각하고
``` python
inorder_idx = {}
for idx,number in enumerate(inorders):
    inorder_idx[number] = idx
```
여기서 딕셔너리를 사용한 것이 문제라고 생각하고 이를 리스트로 바꾸어서 적용  
``` python
inorder_idx = [0 for i in range(n+1)]
for idx,number in enumerate(inorders):
    inorder_idx[number] = idx
```

=> 그래도 문제 발생.....
그래도 메모리 초과가 발생하여 편향된 트리(`skewed tree`)를 넣어보니 무한루프에 빠진 것을 발견  
조건 `     elif start < end  < n:  ` 추가 


# Solution
``` python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
```
## 메모리 할당 List vs Dictionary
``` python
inorder_idx = [0 for i in range(n+1)]
for idx,number in enumerate(inorders):
    inorder_idx[number] = idx
```
딕셔너리로 구현 : `158468KB` , 리스트로 구현 : `154900KB`
리스트가 메모리를 덜 소모되는 것을 확인