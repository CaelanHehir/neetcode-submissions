class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        current = n
        while current != 1 and current not in seen:
            seen.append(current)
            str_number = str(current)
            current = sum(int(digit) ** 2 for digit in str_number)

        return True if current == 1 else False
