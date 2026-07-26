class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        result = [0] * size
        for i in range(size - 1):
            counter = 1
            for j in range(i + 1, size):
                if temperatures[j] > temperatures[i]:
                    result[i] = counter
                    break
                counter += 1

        return result
