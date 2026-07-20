class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        output = []
        for i in range(len(nums)):
            elem = nums[i]
            excluded = [nums[j] for j in range(len(nums)) if j != i]
            product = math.prod(excluded)
            output.append(product)
        return output
