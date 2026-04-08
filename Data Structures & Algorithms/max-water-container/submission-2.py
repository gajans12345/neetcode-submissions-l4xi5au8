class Solution:
    def maxArea(self, height: List[int]) -> int:
        sum1 = 0
        for i in range(len(height)):
            for j in range(len(height)):
                temp  = min(height[i],height[j])
                area = (i - j) * temp
                if area > sum1:
                    sum1 = area
        return sum1
        