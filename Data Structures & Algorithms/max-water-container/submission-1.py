class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height)-1
        a1 = 0
        while a<b:
            area = abs(a-b) * min(height[a],height[b])
            if height[a] < height[b] :
                a = a + 1
            else:
                b = b -1
            if area>a1:
                a1 = area
        return a1


        