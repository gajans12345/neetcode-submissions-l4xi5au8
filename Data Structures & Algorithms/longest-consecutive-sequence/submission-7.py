class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        streak = 1
        max1 = 0
        print(nums)
        for i in range(len(nums)-1):
            print(nums[i])
            if nums[i] +1 == nums[i+1]:
                #print("Incrementing")
                streak+=1
                #print("Streak",streak)
            elif nums[i] == nums[i+1]:
                pass
            else:
                if max1 < streak:
                    max1 = streak
                streak = 1
        if max1 < streak:
            max1 = streak
        return max1
            
            
        