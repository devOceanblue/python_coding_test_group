# 최단 경로
##  1. 한 정점에서 다른 정점(음수 포함 X) - `dijkstra`
<img src="https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif?20171021180030">

### 구현방법
1️⃣ 모든 정점 INF , 출발 노드 설정(0)  
2️⃣ 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택  
3️⃣ 가장 작은 노드와 그 노드에서의 가중치와 비교하여 갱신  
4️⃣ 2️⃣~3️⃣ 반복

### 실행복잡도 일반 -O(V^2) ,heapq 사용- O(ElogV)

- 문제 : https://www.acmicpc.net/problem/1753
``` python
import sys
input = sys.stdin.readline
import heapq


INF = 100_000_000

def get_distance(start,G):
    distance = [INF for _ in range(len(G))]
    distance[start] = 0
    q = []
    heapq.heappush(q,(distance[start],start))
    while q:
        w,v = heapq.heappop(q)
        for node,weight in G[v]:
            if weight+w < distance[node]:
                distance[node] = weight+w
                heapq.heappush(q,(distance[node],node))
    return distance

V,E = map(int,input().split())
G = [[] for _ in range(V)]
start = int(input())-1
for _ in range(E):
    u,v,w = map(int,input().split())
    G[u-1].append((v-1,w))
visited = [0 for _ in range(V)]
distance = get_distance(start,G)
for i in distance:
    if i==INF:
        print("INF")
    else:
        print(i)
```

## 2. 한 정점에서 다른 정점(음수 포함) - `벨만 포드`
<img src= "https://upload.wikimedia.org/wikipedia/commons/7/77/Bellman%E2%80%93Ford_algorithm_example.gif?20210501205439">  

### 구현 방법 
1️⃣ 모든 정점 INF , 출발 노드 설정(0)  
2️⃣ 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택  
3️⃣ 가장 작은 노드와 그 노드에서의 가중치와 비교하여 갱신  
4️⃣ 2️⃣~3️⃣  `V-1`번 반복, 만약 그 후 거리가 갱신된다면 `음수사이클` 발생  

### 시간 복잡도 - O(VE)
### 코드
``` python
isNegCycle = False
for i in range(N):
    for a,b,c in E:
        if dist[a] != INF and dist[b] > dist[a]+c:
            dist[b] = dist[a]+c
            if i==  N-1:
                isNegCycle= True
```

# 3. 모드 정점에서 다른 모든 정점 - `플로이드 워셜`

### 구현 방법
1️⃣ V*V 테이블의 모든 정점 INF , G[i][i] 값 = 0  
2️⃣ 주어진 간선의 값 업데이트  
3️⃣ i -> j로 가는 경우와 i -> k -> j의 경우 중 작은 것으로 업데이트  

### 시간 복잡도 - O(V^3)

### 코드
``` python
G = [[INF for _ in range(N)] for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j],G[i][k]+G[k][j])

```

# 이진 탐색      
<img src ="https://blog.kakaocdn.net/dn/bLB8uL/btqA9ByZ32e/txqBm2qWRb1mz6QHKayLU1/img.gif">

- 배열 내부의 데이터가 `정렬`되어 있을 때만 사용 가능한 알고리즘
- 사용하는 변수 : 시작점, 끝점, 중간점
### 시간 복잡도 - O(logn)
###  코드
``` python
def binary_search(array,target,start,end):
    while start<=end:

        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1 
        else:
            start = mid +1
    return None
```



## lower bound
- `해당 값 이상의 값`이 처음 나오는 인덱스 반환
``` python
def lower_bound(lo,hi,target):
    while lo<=hi:
        m = (lo+hi)//2
        if L[m] < target:
            lo = m +1
        else:
            hi = m-1
    return lo
```

## upper bound
- `해당 값보다 큰 값`이 처음 나오는 인덱스 반환

``` python
def upper_bound(lo,hi,target):
    while lo<=hi:
        m = (lo+hi)//2
        if L[m] <= target:
            lo = m +1
        else:
            hi = m-1
    return lo
```

## decision problem
<img src= "https://user-images.githubusercontent.com/62232531/174028787-01634ae0-fde7-4db1-bd07-cb3df9a52836.png">