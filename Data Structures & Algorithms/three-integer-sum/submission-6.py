class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = {}
        lst1 = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum1 = nums[i] + nums[left] + nums[right]
                if sum1 == 0:
                    temp = [nums[i],nums[left],nums[right]]
                    lst[tuple(temp)] = 0
                    left+=1
                    right-=1
                elif sum1 > 0:
                    right-=1
                elif sum1 < 0:
                    left+=1
        for element in lst:
            lst1.append(list(element))
        return lst1


            
        
        