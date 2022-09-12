# 문제
https://leetcode.com/problems/jump-game-ii/

# 아이디어
앞에 놓여진 도움닫기 발판들중 어떤 발판이 나를 가장 멀리 던져줄수 있는 발판인지를 고른다.
그 다음 발판들에서도 나를 가장 멀리 던져줄수 있는 발판을 고른다.
Greedy하게 나를 가장 멀리 던져줄수있는 발판을 고르다보면 문제의 전제는 무조건 last index에 닿는다고 되어있으므로
최소한의 횟수로 도착할수 있다.

**위 문제는 local optima를 찾으려고 하면 어떻게든 global optima에 도달한다는 문제이다.**

https://www.youtube.com/watch?v=fODpu1-lNTw&ab_channel=DeepLearningAI
![Global-and-local-optima-in-a-search-space-R-n-The-position-on-the-X-and-Y-axis (1)](https://user-images.githubusercontent.com/87791365/178768426-d48a356f-8c08-4bc5-b237-8b394ab17f81.png)


```python
def solution(nums):
    number_of_jumps = 0
    current_jump_limit = 0
    reachable_point = 0
    for i in range(len(nums) - 1):
        reachable_point = max(reachable_point, i + nums[i])
        if i == current_jump_limit:
            number_of_jumps += 1
            current_jump_limit = reachable_point
    return number_of_jumps


if __name__ == "__main__":
    print(solution([2, 3, 1, 1, 4]))

```
