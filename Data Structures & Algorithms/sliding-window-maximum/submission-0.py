class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums) - k + 1 
        maxes = []
        for i in range(size):
            maxes.append(max(nums[i:i + k]))
        return maxes
        