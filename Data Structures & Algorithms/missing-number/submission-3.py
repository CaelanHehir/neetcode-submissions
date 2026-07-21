class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            i += 1
        return i