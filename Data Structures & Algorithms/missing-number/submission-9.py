class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        for i in nums:
            if i != n:
                return n
            n += 1
        return n

    # def missingNumber(self, nums: List[int]) -> int:
    #     nums.sort()
    #     n = 0
    #     for i in nums:
    #         if i == n:
    #             n += 1
    #             continue
    #         return n
    #     return n