

postorder의 경우 left -> right -> root

inorder  
<img src='https://upload.wikimedia.org/wikipedia/commons/4/48/Inorder-traversal.gif'>
postorder   
<img src = 'https://upload.wikimedia.org/wikipedia/commons/2/28/Postorder-traversal.gif'>





<img src ="https://user-images.githubusercontent.com/62232531/176799653-5e8b82a6-bf27-48c4-b0f4-7c5d19df0f73.png">
inorder 결과값을 이용하여 preorder을 구해보자


## Step 1 - 트리의 루트(F)의 왼쪽 자식, 오른쪽 자식 찾기  
<img src="https://user-images.githubusercontent.com/62232531/176800047-e3785017-3d59-4999-8a3e-2059086a9f28.png">

## Step 2 - 왼쪽 서브트리의 루트(B)의 왼쪽, 오른쪽 자식 찾기  
<img src = "https://user-images.githubusercontent.com/62232531/176800450-7e670f05-6066-419e-b9cc-5409b4065bf6.png">

## Step 3 - 오른쪽 서브트리의 루트(D)의 왼쪽, 오른쪽 자식 찾기  
<img src = "https://user-images.githubusercontent.com/62232531/176800919-da019a62-ddd9-4474-806d-3d2214e2aa2a.png">

##  모든 노드를 탐색할때까지 반복..

## 아이디어 - inorder 결과값을 이용하여 preorder 출력
1. 트리의 루트를 출력하자  (root)
2. 왼쪽트리의 루트를 출력하자 (left)
3. 오른쪽트리의 루트를 출력하자 (right)


## inorder의 루트 인덱스 찾기
``` python
inorder_idx = {}
for idx,number in enumerate(inorders):
    inorder_idx[number] = idx
```
트리의 postorder 마지막 결과값이 `root`라는 것을 이용  
inorder_idx[root] => 해당 트리의 root 인덱스

## inorder과 postorder 비교
<img src = "https://user-images.githubusercontent.com/62232531/176801976-8cb1b8c7-3793-495c-bb55-96b60b74472f.png">
왼쪽 자식의 경우 위치는 그래도지만 오른쪽 자식의 경우 1칸 당겨짐 -> depth 만큼 반복됨






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