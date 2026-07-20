class Solution:
    def get_first_wall(self, height: list[int], start: int) -> int:
        for i in range(start, len(height) - 1):
            if height[i] > height[i + 1]:
                return i

        return -1


    def get_second_wall(self, height: list[int], first_wall: int) -> int:
        if first_wall == -1:
            return -1

        wall_value = -1
        wall_index = -1
        for i in range(first_wall + 1, len(height)):
            if height[i] > wall_value:
                wall_value = height[i]
                wall_index = i
            if wall_value >= height[first_wall]:
                return wall_index


        return wall_index


    def get_area(self, height: list[int], first_wall: int, second_wall: int) -> int:
        count = 0
        for i in range(first_wall + 1, second_wall):
            count += min(height[first_wall], height[second_wall]) - height[i]

        return count


    def trap(self, height: list[int]) -> int:
        current = 0
        filled = 0
        while current < len(height):
            first_wall = self.get_first_wall(height, current)
            second_wall = self.get_second_wall(height, first_wall)
            if first_wall == -1 or second_wall == -1:
                break
            filled += self.get_area(height, first_wall, second_wall)
            current = second_wall

        return filled