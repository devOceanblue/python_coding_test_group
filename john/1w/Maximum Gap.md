# Maximum Gap

## Explain Problem

<https://leetcode.com/problems/maximum-gap/>

* Tag
  * Array
  * Sorting
  * Bucket Sort
  * Radix Sort
* Acceptable : 41.7%
* Difficulty : Hard

1개의 정렬이 되지 않은 무작위 배열이 주어지게 되고,  
해당 배열에서 제일 Gap차이가 큰 수를 찾아 그 값을 리턴해야한다

## Solution

처음에 제출한 솔루션은 단순하게 Sort()함수를 적용하여 순서대로 배열을 분배하고,  
배열의 앞, 뒤를 탐색하며 크기가 제일 큰 수를 return하는 방법으로 생각했다.

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_num = 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > max_num:
                max_num = nums[i+1] - nums[i]
        return max_num
```

실행 결과는 다음과 같았습니다.  

* Runtime: 1497 ms, faster than 55.43% of Python3 online submissions for Maximum Gap.
* Memory Usage: 28.1 MB, less than 69.96% of Python3 online submissions for Maximum Gap.

일단 이렇게 해결할 경우에는 시간 복잡도는 Tim sort로 인해서  
O(nlogn)이라고 생각하고 공간복잡도의 경우에는 O(n/2)라고 생각했다.

이렇게 쉬운게 Hard난이도일리 없는데 하면서, 해당 문제의 Tag를 확인했고,
Bucket Sort인것을 확인하고 그것에 대해 알아봤다.

## Bucket Sort

![image](https://media.geeksforgeeks.org/wp-content/uploads/BucketSort.png)

* 데이터 𝑛개가 주어졌을 때 데이터의 범위를 𝑛개로 나누고 이에 해당하는 𝑛개의 버킷을 만든다.
* 각각의 데이터를 해당하는 버킷에 집어 넣는다. (C 등에서는 연결리스트를 사용하며 새로운 데이터는 연결리스트의 head에 insert한다)
* 버킷별로 정렬한다.
* 이를 전체적으로 합친다.

이 문제 기준으로 정렬을 하면 조건은 다음과 같다.

* 배열의 숫자를 n, 배열의 max값, 배열의 min값을 조사 <https://wiki.python.org/moin/TimeComplexity>
* max값과 min값의 차를 계산하여 n으로 나누고 bucket을 생성함
* bucket간의 거리가 먼 숫자가 제일 차이가 큰 값
* 최악의 케이스
  * 모든 bucket에 숫자가 하나씩 배정되는 경우
  * 시간복잡도는 O(n), 공간복잡도는 O(n)이라고 생각했다.

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        B = defaultdict(list)
        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            B[ind].append(num)
            
        cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        return max(y[0]-x[1] for x,y in zip(cands, cands[1:]))
```

근데....

* Runtime: 2264 ms, faster than 20.63% of Python3 online submissions for Maximum Gap.
* Memory Usage: 52.5 MB, less than 5.13% of Python3 online submissions for Maximum Gap.

의도한 대로 풀긴 했는데 ㅠ 생각보다 효율이 안좋은 것을 확인했다.  
아무래도 dictionary를 생성하고 생성된 dictionary에서 다시 max, min을 출력하는 candidates list를 만들고,  
거기서 max값을 출력하는 방식이 조금 시간을 잡아먹은듯 한다.

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        bucket_max = [0] * n
        bucket_min = [10**9+1] * n
        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            bucket_max[ind] = max(num, bucket_max[ind])
            bucket_min[ind] = min(num, bucket_min[ind])
        
        maxgap = 0
        # consider min
        previous = lo
        for i in range(n-1):
            if bucket_min[i] == 10**9+1 and bucket_max[i] == 0:
                #empty bucket
                continue
            maxgap = max(maxgap, bucket_min[i] - previous)
            previous = bucket_max[i]
        #consider max
        maxgap = max(maxgap, hi - previous)
        return maxgap
```

* Runtime: 1953 ms, faster than 30.28% of Python3 online submissions for Maximum Gap.
* Memory Usage: 27.3 MB, less than 94.14% of Python3 online submissions for Maximum Gap.

큰 차이는 없었지만 팀 소트에 비해 메모리 사용량은 줄어든 것을 확인할수 있었고,  
시간에 대해서는 조금 느리긴 했는데, 그래도 기존 dictionary를 사용한 것보다는 빨라지며, 약 10퍼센트의 증가를 보였다.  

## Reference

<https://ratsgo.github.io/data%20structure&algorithm/2017/10/18/bucketsort/>
