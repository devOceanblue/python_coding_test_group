# Valid Number

## Explain Problem

<https://leetcode.com/problems/valid-number/>

* Tag
  * String
* Acceptable : 18.3%
* Difficulty : Hard

1개의 정렬이 되지 않은 무작위 배열이 주어지게 되고,  
해당 배열에서 제일 Gap차이가 큰 수를 찾아 그 값을 리턴해야한다

```plain
A valid number can be split up into these components (in order):

1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

1. (Optional) A sign character (either '+' or '-').
2. One of the following formats:
  1. One or more digits, followed by a dot '.'.
  2. One or more digits, followed by a dot '.', followed by one or more digits.
  3. A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

1. (Optional) A sign character (either '+' or '-').
2. One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
```

## Solution

첫번째 든 생각은 일단 regular expression을 통해 문제를 풀어야되는가 생각하고 문제를 풀었다.

```python
class Solution(object):
    def isNumber(self, s):
        regex = r"[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?"
        if not re.findall(regex, s):
            return False
        try:
            float(s)
        except:
            return False
        return True
```

* Runtime: 24 ms
* Memory Usage: 13.6 MB

이렇게 될 경우에는 문제가 너무 쉽기 때문에...  
이렇게 푸는 문제는 아닐거라고 생각하고 최대한 정규식과 비슷하게 string parsing을 하면 될것이다 라고 판단했다.  

기준을 보면 부호(sign), 숫자(digit), 지수(exponential), 소수점(dot) 4가지로 나뉘게 된다.  
이중에 지수를 기준으로 한번씩 더 쓰일 가능성이 있으므로, 지수 기준으로 한번씩 더 counting할수 있도록 해야한다.  
예외로 지수 뒤에는 소수점은 인정되지 않는다.  

이것을 코드로 옮기게 되면 다음과 같다.

```python
class Solution:
    def isNumber(self, S: str) -> bool:    
        exp, digit, sign, dot = False, False, False, False
        for c in S:
            if c >= '0' and c <= '9': 
                digit = True     
            elif c == 'e' or c == 'E':
                if exp or not digit: 
                    return False
                else: 
                    exp, digit, sign, dot = True, False, False, False
            elif c == '+' or c == '-':
                if sign or digit or dot: 
                    return False
                else: 
                    sign = True
            elif c == '.':
                if dot or exp: 
                    return False
                else: 
                    dot = True
            else: 
                return False
        return digit
```

* Runtime: 59 ms
* Memory Usage: 14 MB

속도는 조금 느렸지만, 출제 의도 대로 문제를 풀게 되었다.  
