class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encountered = []
        for num in nums:
            if num in encountered:
                return True
            encountered.append(num)

        
        return False