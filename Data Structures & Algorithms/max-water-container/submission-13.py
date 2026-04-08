class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVol = 0
        volume = 0
        while left < right:
            
            if height[left] <= height[right]:
                volume = height[left] * (right - left)

            else:
                volume  = height[right] * (right - left)
            print(left,right,volume)
            if volume > maxVol:
                maxVol = volume
            if height[left] < height[right]:
                left+=1
                
            else:
                right-=1
        return maxVol
            
    


        





        
        