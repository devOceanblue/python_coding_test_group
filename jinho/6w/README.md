# 힙구조
- 힙의 특성을 만족하는 트리 기반의 자료구조.
- 최댓값과 최솟값을 찾아내는 연산을 빠르게 하기 위해 힙으로 구현하지만, 주의할 점은 힙 자체는 `정렬`이 되어있지 않다.

## 특성
- 최소힙(Min Heap) : 부모 노드가 자식노드 값보다 항상 작음
- 최대힙(Max Heap) : 부모 노드가 자식노드 값보다 항상 큼

## 삽입(push)
<img src ="https://miro.medium.com/max/1920/1*jeELUYrAVbZJg6S1E2ujjA.gif">
삽입의 경우 마지막 노드 뒤에 삽입을 한 뒤 min-heap 적용 O(logN)

## 삭제(pop)

<img src="https://miro.medium.com/max/700/1*j6SmjQvS1-FPcONVtEkN1w.gif">
삭제의 경우 루트 노드와 마지막 노드를 스왑한 뒤 루트에서부터 min-heap 적용 O(logN)


|메소드|시간복잡도
|-----|---------|
|heappush|O(logN)|
|heappop|O(logN)|
|heappushpop|O(logN)|
|heapify|O(NlogN)|


# heap정렬
 heap정렬은 max-heap 구조에서 pop을 n만큼 반복시킨 것  시간복잡도 : O(NlogN)
