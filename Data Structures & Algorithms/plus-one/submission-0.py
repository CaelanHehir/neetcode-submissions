class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        while digits:
            number = number * 10 + digits[0]
            digits.remove(digits[0])
        number += 1

        str_number = str(number)
        return [int(digit) for digit in str_number]