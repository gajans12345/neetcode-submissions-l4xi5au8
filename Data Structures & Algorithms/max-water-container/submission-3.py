class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        area = 0
        for i in range (len(height)):
            for j in range (i+1,len(height)):
                if height[i] >= height[j]:
                    area = (j - i) * height[j]
                else:
                    area = (j - i) * height[i]
                if area > maxArea:
                    maxArea = area
        return maxArea


        
        