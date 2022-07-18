# Tim Sort

python에서 사용하는 list.sort()나 sorted()함수에서 적용되는 정렬 함수는 Tim sort방식을 취하고 있습니다.  
이 정렬을 알아보면서 Tim sort는 어떤식으로 정렬하는지에 대해 알아보겠습니다.

## 알고리즘의 조합

알고리즘의 이론적인 증명에 대해서는 키워드는 4개의 키워드를 생각하시면 될거같습니다.

* 참조 지역성(Locality of reference) 원리
* **Quick sort**보다 빠르게 구현할수있는
  * **Merge sort**
* **Insertion sort**

![image](https://d2.naver.com/content/images/2020/01/img.png)

시간 복잡도가 O(nlogn)이라는 말은 실제 동작 시간은 C × nlogn + α  
이 C라는 값에 큰 영향을 끼치는 요소로 '알고리즘이 참조 지역성(Locality of reference) 원리를 얼마나 잘 만족하는가'

Insertion sort의 상수 C를 Ci, O(nlogn) 정렬 알고리즘 중 C값이 가장 작다고 알려져 있는 Quick sort의 상수 C를 Cq라 할 때, 작은 n에 대하여 Ci × n^2 > Cq × nlogn이 성립한다.  
즉, 작은 nn에 대하여 Insertion sort가 빠르다는 것

2^x개씩 잘라 각각을 Insertion sort로 정렬하면 일반적인 Merge sort보다 덩어리별 x개의 병합 동작이 생략되어,  
Merge sort의 동작 시간을 Cm × nlogn이라 할 때 Tim sort의 동작 시간은 Cm × (nlogn - x) + α가 된다.  
이때의 x값을 최대한 크게 하고 α값을 최대한 줄이기 위해 여러 가지 최적화 기법이 사용된다.

## 최적화 방법

### Run

첫 두 원소의 대소 관계로 이 덩어리를 증가하는 덩어리, 감소하는 덩어리로 정의하여 2^x개까지는 Insertion sort를 진행하고  
그 이후의 원소에 대해서 가능한 한 크게 덩어리를 만든다. 이런 덩어리를 run이라고 부르며 이때의 2^x를 minrun  
증가하는 run: a_0 <= a_1 <= a_2 <= a_3 <= ...a  
감소하는 run: a_0 > a_1 > a_2 > a_3 > ...a  

### Binary Insertion sort

삽입해야 할 위치를 찾을 때까지 비교하는 대신, 앞의 원소들은 모두 정렬되어 있다는 전제를 기반으로 이분 탐색을 진행하여 위치를 찾는다.  
이분 탐색은 참조 지역성은 떨어지지만 한 원소를 삽입할 때 O(n)번의 비교를 진행하는 대신 O(logn)번의 비교를 진행하기에 작은 n에 대하여 좀 더 시간을 절약할 수 있다.  

```python
def insertion_sort(arr):
    print(arr)
    for end in range(1, len(arr)):
        print(f'round {end}')
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            print(locals())

def binary_insertion_sort(arr):
    print(arr)
    for end in range(1, len(arr)):
        print(f'round {end}')
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            print(locals())
```

### Merge

![image](https://d2.naver.com/content/images/2020/01/img-6-.png)

![image](https://d2.naver.com/content/images/2020/01/img-7-.png)

첫 번째 장점은 스택에 들어있는 run의 수를 작게 유지할 수 있다는 것이다.
원소를 추가할 때에도 이 조건에 맞게 유지를 하니 결국 스택에 있는 모든 run은 2보다 같거나 큰 i에 대해 C > A + B를 만족한다.

두 번째 장점은 비슷한 크기의 덩어리와 병합할 수 있다는 것이다.  
조건을 만족하지 않을 경우 B는 A와 C 중 작은 run과 병합한다고 했는데 이는 BB에서 인접한 두 run을 모두 확인하여 그 중 가장 비슷한 run과 병합한다는 것이다.  
최소한의 메모리를 이용하여 최고의 효율을 내기 위한 방법이다.

### 2 Run Merge

![image](https://d2.naver.com/content/images/2020/01/img-9-.gif)
두 run 중 크기가 작은 run을 담을 메모리가 필요하기에 병합을 진행할 때 최악의 경우 n/2의 추가 메모리를 사용하는 것을 알 수 있다.  
비록 Merge sort와 같은 O(n)O(n)의 추가 메모리를 사용하지만 절반을 절약
병합하기 전, 병합을 수행할 필요가 없는 구간을 먼저 계산

### Galloping

Galloping mode(질주 모드)일 경우 하나의 run을 빠르게 참조하도록 동작
처음에는 화살표가 가리키고 있는 두 원소를 대소 비교를 하여 어느 run의 원소를 넣을지 정한다. 이 때의 방법을 One pair at a time mode
3번 연속으로 병합되었기에 Galloping mode로 전환
2^k로 뛰어 넘으며 대소 비교를 진행
하나의 run에서 연속적으로 병합되지 않을 경우 One pair at a time mode로 돌아가 다시 하나씩 비교를 진행
실제 코드에서는 MIN_GALLOP번 연속으로 한 run에서 병합되었을 경우 Galloping mode로 전환하며 MIN_GALLOP는 전체 배열을 정렬하는 과정에서 Galloping mode에 들어가는 횟수가 많았다면 감소하고 아니라면 증가하여 좀 더 효율적으로 동작

## Reference

Tim sort에 대해 알아보자
<https://d2.naver.com/helloworld/0315536>
