class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        index = 1
        start = intervals[0][0]
        end = intervals[0][1]
        merged = list()
        while 1:
            if intervals[index][1] < end:
                index += 1
                if index == len(intervals):
                    merged.append([start, end])
                    break
                continue
            if intervals[index][0] < end:
                end = intervals[index][1]
            else:
                merged.append([start, end])
                start = intervals[index][0]
                end = intervals[index][1]
            index += 1
            if index == len(intervals):
                merged.append([start, end])
                break
        return merged
        

test = [[1,4],[2,3]]
s = Solution()
r1 = s.merge(test)
print(r1)