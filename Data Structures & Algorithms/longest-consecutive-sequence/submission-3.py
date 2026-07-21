class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        lis = [1] * size
        nums = sorted(nums)

        for i in range(1, size):
            for prev in range(0, i):
                if nums[prev] + 1 == nums[i]:
                    lis[i] = max(lis[i], lis[prev] + 1)

        return max(lis)
