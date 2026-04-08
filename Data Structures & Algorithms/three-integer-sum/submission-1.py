class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        dict1 = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and i != k:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        if tuple(temp) not in dict1.keys():

                            lst.append(temp)
                            dict1[tuple(temp)] = 0
        return lst
        