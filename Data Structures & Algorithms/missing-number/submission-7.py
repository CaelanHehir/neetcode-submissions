class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for _ in range(len(nums)):
            if nums[i] != i:
                return i
            i += 1
        return i

    # def missingNumber(self, nums: List[int]) -> int:
    #     nums.sort()
    #     n = 0
    #     for i in nums:
    #         if i == n:
    #             n += 1
    #             continue
    #         return n
    #     return n