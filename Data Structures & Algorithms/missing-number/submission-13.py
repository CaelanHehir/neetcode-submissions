class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        nums.sort()
        for i in nums:
            if i == n:
                n += 1
                continue
            return n
        return n
