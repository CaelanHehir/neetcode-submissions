class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for number in range(n + 1):
            binary = bin(number)
            output.append(binary.count('1'))
        return output
        