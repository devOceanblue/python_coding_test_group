# 문제
https://leetcode.com/problems/binary-tree-maximum-path-sum/solution/

# 아이디어

재귀(Recursion)를 사용해서 현재 노드를 중심으로 경로의 최댓값을 찾는다.  
현재노드 + 왼쪽 또는 현재노드 + 오른쪽 경로의 최댓값을 리턴해서 부모노드에게 반환한다.  

<img width="254" alt="스크린샷 2022-07-14 오후 1 19 19" src="https://user-images.githubusercontent.com/87791365/178898075-e3070f87-1614-47d4-aa3a-3e9844e29092.png">
<img width="252" alt="스크린샷 2022-07-14 오후 1 19 23" src="https://user-images.githubusercontent.com/87791365/178898083-cc9dd604-5068-4c7d-bce7-de86530bd544.png">
<img width="242" alt="스크린샷 2022-07-14 오후 1 19 28" src="https://user-images.githubusercontent.com/87791365/178898096-2c1ef99f-6192-4975-9cec-c82e2cc58ff4.png">
<img width="244" alt="스크린샷 2022-07-14 오후 1 19 31" src="https://user-images.githubusercontent.com/87791365/178898102-9f4ae75d-e033-4ff2-a5d5-640abeddcda1.png">
<img width="236" alt="스크린샷 2022-07-14 오후 1 19 35" src="https://user-images.githubusercontent.com/87791365/178898112-1cc7824a-af6b-4eab-ae6e-2865c6ecee93.png">
<img width="244" alt="스크린샷 2022-07-14 오후 1 19 38" src="https://user-images.githubusercontent.com/87791365/178898124-7d13dabb-68b3-45f7-8ff1-3c4326f259c0.png">
<img width="226" alt="스크린샷 2022-07-14 오후 1 19 42" src="https://user-images.githubusercontent.com/87791365/178898129-5672dce7-ffbd-471d-a550-2bad33b2a778.png">


```python
class Solution:
    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        max_gain(root)
        return max_sum


```
