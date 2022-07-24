# Longest Binary Subsequence Less Than or Equal to K

## Explain Problem

<https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/>

* Tag
  * String
  * Dynamic Programming
  * Greedy
  * Memoization
* Acceptable : 33.9%
* Difficulty : Medium

Binary String인 s와 integer숫자인 k가 주어지게 되고,
k 숫자보다 작거나 같은 binary숫자 조합을 찾고, 그 string의 길이를 반환해야된다.

```plain
Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
```

```plain
Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
```

## Solution

일단 해당 문제는 중간에 끝내는 방식을 취하게 되면 너무 많은 경우가 해당이 된다고 생각했다.  
제일 먼저 든 생각은 queue를 이용해서, 0을 집어넣다가, k에 해당하는 binary length에 도달했을때부터 정지하고 숫자를 집어넣어야 한다고 생각하고 진행하려고 했으나,
로직이 잘 떠오르지 않았고, 다른 방법을 다시 생각해봤다.  

일단 결과적으로는 k를 binary string으로 치환한 뒤에 k값과 s값의 [-length(k):]값을 자른 만큼의 숫자를 비교한뒤에  
앞에 0개수만 덧붙이면 된다는 생각을 하고 문제를 풀었다.

```python
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        binary_str = "{0:b}".format(k)
        max_binary_length = len(binary_str)
        if max_binary_length > len(s):
            return len(s)
        if binary_str >= s[-max_binary_length:]:
            return s[:-max_binary_length].count("0") + max_binary_length
        else:
            return s[:-max_binary_length + 1].count("0") + max_binary_length - 1
```

* Runtime: 54 ms
* Memory Usage: 13.9 MB
