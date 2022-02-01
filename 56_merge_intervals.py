class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]
        for interval in intervals:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged
        

test = [[1,4],[2,3]]
s = Solution()
r1 = s.merge(test)
print(r1)