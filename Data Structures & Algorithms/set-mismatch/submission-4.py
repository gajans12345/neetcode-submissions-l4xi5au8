class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict1 = {}
        missing = 0
        duplicate = 0
        for i in range(1,len(nums)+1):
            dict1[i] = 0
        for element in nums:
            dict1[element]+=1 #{1:1,2:2,3:0,4:1}
        result = []
        for key,value in dict1.items():
            if value == 0:
                missing = key
            if value > 1:
                duplicate = key
        result = [duplicate,missing]
        return result
        