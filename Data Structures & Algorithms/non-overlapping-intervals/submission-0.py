class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        prevEnd = intervals[0][1]
        count = 0
        for a,b in intervals[1:]:
            if a < prevEnd:
                count += 1
            else:
                prevEnd = b
        return count

        
        