class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        lst = [0]*len(nums)
        lst2 = []
        temo = nums
        for i in range(len(nums)):
            if nums[i]== 0:
                lst2.append(i)
                product *=1
                
            else:
                product *=nums[i]
            
        if len(lst2) == 0:
            for i in range(len(nums)):
                lst[i] = product // nums[i]
        elif len(lst2) == 1:
            lst[lst2[0]] = product
        return lst
        