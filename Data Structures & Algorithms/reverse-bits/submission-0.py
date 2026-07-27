class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = ["0"] * 32
        binary = bin(n).removeprefix("0b")
        i = 0
        for j in range(len(binary) - 1, -1, -1):
            reverse[i] = binary[j]
            i += 1
        reverse = "".join(reverse)
        return int(reverse, 2)