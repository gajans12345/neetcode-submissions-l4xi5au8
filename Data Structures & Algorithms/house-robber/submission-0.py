class Solution:
    def rob(self, nums: List[int]) -> int:
        grid = [0] * (len(nums) + 1) 
        if len(nums) == 0:
            return 0
        grid[0] = 0
        grid[1] = nums[0]
        if len(nums) == 1:
            return nums[0]
        grid[2] = max(nums[0],nums[1])
        if len(nums) == 2:
            return max(nums[0],nums[1])
        for i in range(3,len(nums)+1):
            grid[i] = max(grid[i-1],grid[i-2]+nums[i-1])
        print(grid)
        return grid[-1]