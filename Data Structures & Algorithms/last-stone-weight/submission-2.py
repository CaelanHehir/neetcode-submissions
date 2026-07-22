class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heaviest = max(stones)
            stones.remove(heaviest)
            second_heaviest = max(stones)
            stones.remove(second_heaviest)

            if heaviest == second_heaviest:
                continue
            else:
                stones.append(heaviest - second_heaviest)

        if not stones:
            return 0

        return stones[0]
