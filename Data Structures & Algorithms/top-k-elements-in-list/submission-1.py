class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        top = []
        counts = dict()
        uniques = {elem for elem in nums}
        for number in uniques:
            occurences = nums.count(number)
            counts[number] = occurences

        for _ in range(min([k, len(nums)])):
            maxi = 0
            maxi_occurences = float('-inf')
            for number in counts:
                if counts[number] > maxi_occurences:
                    maxi = number
                    maxi_occurences = counts[number]
            top.append(maxi)
            counts[maxi] = -1

        return top
