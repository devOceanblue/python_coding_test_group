import sys
import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        ans = 1
        meeting_rooms = [0]
        for meeting in intervals:
            if meeting[0] > meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            else:
                ans += 1
            heapq.heappush(meeting_rooms, meeting[1])
        return ans
