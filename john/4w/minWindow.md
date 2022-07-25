# minWindow

## Explain Problem

[Minimum Window Substring - LeetCode](https://leetcode.com/problems/minimum-window-substring/)

* Tag
  * Hash Table
  * String
  * Sliding Window
* Acceptable : 39.4%
* Difficulty : Hard

```plain
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Solution

Streaming 환경에서 사실 window의 개념은 하루이틀 보는게 아니였다.

[Windows | Apache Flink](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/operators/windows/#sliding-windows)

그중에서 sliding windows라는 개념이 있는데, 여기서는 특정 윈도우 사이즈만큼 통과하는 양을 윈도우 슬라이드만큼 표시할수 있다 정도의 개념으로 설명하고 있다.

일단 문제로 다시 돌아가서.
기본적으로는 t에서 각 문자열이 몇개가 들어가있는지 중요하기 때문에
Counter를 이용해서 각 문자열의 개수를 확인한다.
(Hash Table)

그 이후 Two Pointer를 이용한다.
출력을 하기 위해서 제일 minimum사이즈로 표현되어야 하는 시작점과 끝점
그리고 window를 늘리고 줄이는 current window i,j값으로 표현하고
j가 늘어날때마다 Counter로 세었던 각 요소들을 -1하면서 카운팅하고  (이때 음수값으로 가도 무시해야된다.)
전체 t의 크기(모든 요소들이 다 들어갔다는 전제)를 확인하고 그것도 -1을 카운팅한다

지금까지 설명한 것을 다시 정리하면

* Counter를 이용, t값의 각 요소의 개수를 확인한다.
  * ex) t="ABC"
    * Counter({'B': 1, 'C': 1, 'A': 1})
    * missing = len(t)
* i, j = 현재 슬라이딩, start, end = 슬라이딩 윈도우의 최소값이며, 더 작은 차이가 발생할 경우 갱신한다.
* 각 요소가 들어갈때마다missing--를 하고, 전부 들어갔다고 판단(missing == 0)되면 좌측 슬라이딩 윈도우를 땡긴다.
  * 기본적으로 j, end는 우측 슬라이드, i, start는 좌측 슬라이드이다.

```python
class Solution:
    def minWindow(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1
                missing += 1
                if end == 0 or j-i < end-start:
                    start, end = i, j
                i += 1
        return s[start:end]
```
