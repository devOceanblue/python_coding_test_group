# 문제
https://leetcode.com/problems/merge-k-sorted-lists/solution/

# 아이디어

여러개의 Linkedlist를 정렬하여 하나로 병합하는 문제이다.
삽입정렬을 사용하여 간단하게 해결할수 있다.


<img width="587" alt="스크린샷 2022-07-14 오후 1 54 18" src="https://user-images.githubusercontent.com/87791365/178902422-b38b1854-6b5b-4cfd-a7aa-2a3ca8a4c14c.png">


```python
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertion_sort(self, lists):
        node = root = ListNode(0)

        for i in range(len(lists)):
            head = lists[i]
            while head:
                while node.next and head.val >= node.next.val:
                    node = node.next

                node.next, head.next, head = head, node.next, head.next
                node = root

        return node.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        lists = [i for i in lists if i != None]

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        result = None
        if len(lists) > 1:
            result = self.insertion_sort(lists[:])
        return result


if __name__ == "__main__":
    first = ListNode(1)
    first.next = ListNode(4)
    first.next.next = ListNode(5)

    second = ListNode(1)
    second.next = ListNode(3)
    second.next.next = ListNode(4)

    third = ListNode(2)
    third.next = ListNode(6)

    sol = Solution()
    result = sol.mergeKLists([first, second, third])
    while result:
        print(result.val)
        result = result.next

```
