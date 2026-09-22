class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict1={}
        temp = []
        count
        for element in nums:
            if element in dict1:
                dict1[element]+=1
            else:
                dict1[element] = 1
        for key,value in dict1.items():
            temp.append(key)
        nums[:] = temp
        return len(nums)


        


        