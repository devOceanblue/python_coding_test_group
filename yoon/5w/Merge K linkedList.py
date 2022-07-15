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
