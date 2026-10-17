"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda item: item.start)

        # min-heap of room end times
        ends = []  

        for i in intervals:
            if ends and ends[0] <= i.start:
                # earliest-ending room is free
                heapq.heapreplace(ends, i.end)
            else:
                # no room free, open a new one
                heapq.heappush(ends, i.end)

        return len(ends)

        