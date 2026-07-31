class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        values = set()
        for num in nums:
            if num in values:
                return num
            values.add(num)
        return -1
