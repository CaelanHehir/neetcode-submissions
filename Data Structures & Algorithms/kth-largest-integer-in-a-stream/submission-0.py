class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)

        ordered = sorted(self.nums)
        for _ in range(self.k - 1):
            ordered.pop()
        return ordered[len(ordered) - 1]

        
