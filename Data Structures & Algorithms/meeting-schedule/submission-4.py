"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prev_end = intervals[0].end
        # print("prev_end:" + str(prev_end))
        for interval in intervals[1:]:
            a = interval.start
            # print("a:" + str(a))
            b = interval.end
            if a < prev_end:
                return False
            prev_end = b
        return True

(0, 3), (3, 6), (5, 10)