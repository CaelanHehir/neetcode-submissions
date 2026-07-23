class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for number in set(nums):
            if nums.count(number) == 1:
                return number
