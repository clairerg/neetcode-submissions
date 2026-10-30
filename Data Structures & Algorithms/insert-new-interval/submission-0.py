class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a = newInterval[0]
        b = newInterval[1]
        final_interval = []
        inserted = False
        for start, end in intervals:
            if b < start:
                if not inserted:
                    final_interval.append([a, b])
                    inserted = True
                final_interval.append([start, end])
            elif a > end:
                final_interval.append([start, end])
            else:
                a = min(a, start)
                b = max(b, end)
        if not inserted:
            final_interval.append([a, b])
        return final_interval

        