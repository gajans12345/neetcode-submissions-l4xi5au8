class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] >= intervals[i][0]:            # overlaps: extend curr
                curr = [curr[0], max(curr[1], intervals[i][1])]
            else:                                      # gap: curr is finished
                res.append(curr)
                curr = intervals[i]
        res.append(curr)                               # save the last one
        return res