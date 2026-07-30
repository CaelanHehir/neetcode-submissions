class Solution:
    def check_overlap(self, interval1: List[int], interval2: List[int]) -> bool:
        start1, end1 = interval1[0], interval1[1]
        start2, end2 = interval2[0], interval2[1]

        return (start1 <= start2 <= end1) or (start2 <= start1 <= end2)


    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = intervals
        intervals.sort()
        print(merged)
        i = 0
        while i < len(merged) - 1:
            if self.check_overlap(merged[i], merged[i + 1]):
                start = min(merged[i][0], merged[i + 1][0])
                end = max(merged[i][1], merged[i + 1][1])
                merged[i] = []
                merged[i + 1] = [start, end]
            i += 1

        merged = [interval for interval in merged if interval]
        return merged

        return merged

        return merged