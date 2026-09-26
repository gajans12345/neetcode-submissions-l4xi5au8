class Solution:
    def trap(self, height: List[int]) -> int:
        #[1,5,2,3,4] note prefix depends on previous so loop right,suffix oppo
        water = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[0] = height[0]
        currMax = prefix[0]
        for i in range(1,len(height)):
            prefix[i] = max(height[i],currMax)
            if height[i] > currMax:
                currMax = height[i]
        currMx = height[-1]
        suffix[-1] = currMx
        for i in range(len(height) - 1,-1,-1):
            suffix[i] = max(currMx,height[i])
            if currMx < height[i]:
                currMx = height[i]
        for i in range(len(height)):
            water+= min(suffix[i],prefix[i]) - height[i]
        return water
            
                

        
        