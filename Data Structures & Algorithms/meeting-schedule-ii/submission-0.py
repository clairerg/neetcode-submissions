"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq 
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            a = interval.start
            b = interval.end
            if not heap:
                heapq.heappush(heap, b)
            elif a < heap[0]:
                heapq.heappush(heap, b)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, b)
        return len(heap)
        


        