# Find Median from Data Stream

## Explain Problem

<https://leetcode.com/problems/find-median-from-data-stream/>

* Tag
  * Two Pointers
  * Design
  * Sorting
  * Heap (Priority Queue)
  * Data Stream
* Acceptable : 50.5%
* Difficulty : Hard

* 중앙 값을 출력하는데, 정확히 중앙값이 안나올경우 중앙의 앞뒤 값의 평균을 출력해야한다.
* Example
  * For example, for arr = [2,3,4], the median is 3.
  * For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

## Solutions

* 일단 2가지를 생각
  * 처음에 입력할때는 정렬하지 않고, 순차적으로 list만 생성, 중앙값을 찾을때 Tim sort를 이용하여 결과를 출력
  * 데이터를 삽입할때부터 heapq를 이용하고, 출력할때는 kth_smallest를 이용하여 출력?

```python
class MedianFinder:
    nums = None
    def __init__(self):
        self.nums = list()

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        return self.nums[(len(self.nums)-1)//2] \
                    if (len(self.nums) - 1) % 2 == 0 \
                    else (self.nums[(len(self.nums)-1) // 2] + self.nums[(len(self.nums)-1) // 2 + 1]) / 2
```

* Runtime: 4277 ms, faster than 5.00% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 36.2 MB, less than 47.35% of Python3 online submissions for Find Median from Data Stream.

Priority Queue로 구성할때는 효율적으로 생각하려면, 몇가지 트릭이 필요한데,  

* heapq에서 첫번째 배열은 무조건 제일 작은 값이다.
* 음수값을 잘 이용하면 큰 수가 제일 앞으로 오게 할수있다.

* large배열을 만들고 항상 양수값을 집어넣으면 맨 앞에 배열은 가장 작은 값이 들어간다.
* small배열을 만들고 항상 음수값을 집어넣으면 맨 앞에 배열은 가장 큰 값의 음수값이 들어간다.
* heappushpop을 이용해, 값을 집어넣으면서 매번 작은(혹은 음수로 큰) 값인지 비교하며 확인하는 과정을 만든다.

```python
from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
```

* Runtime: 845 ms, faster than 38.89% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 36.1 MB, less than 47.35% of Python3 online submissions for Find Median from Data Stream.

## Reference

[파이썬] heapq 모듈 사용법  
<https://www.daleseo.com/python-heapq/>

[Java] PriorityQueue(우선순위 큐) 클래스 사용법 & 예제 총정리  
<https://coding-factory.tistory.com/603>
