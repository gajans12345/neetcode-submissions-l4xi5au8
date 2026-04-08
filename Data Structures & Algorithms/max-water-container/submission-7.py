class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        area = 0
        a = 0
        b = len(height) - 1
        while a < b:
            if height[a] <= height[b]:
                area = (b - a) * height[a]
            elif height[a] > height[b]:
                area = (b - a) * height[b]
            if area > maxArea:
                maxArea = area
            if height[b] >= height[a]:
                a = a + 1
            elif height[b] < height[a] :
                b = b - 1
        return maxArea

        





        
        