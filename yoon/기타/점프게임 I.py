from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable = 0
        for i in range(n):
            if i > reachable:
                return False
            if reachable >= n:
                return True
            reachable = max(reachable, i + nums[i])
        return True
