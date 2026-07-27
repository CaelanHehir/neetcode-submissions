class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for starting_index in range(len(gas)):
            car = 0
            current = starting_index
            for _ in range(len(gas)):
                car += gas[current]
                car -= cost[current]
                current += 1
                if current >= len(gas):
                    current = 0
                if car < 0:
                    break
                if current == starting_index:
                    return starting_index
        return -1
                
