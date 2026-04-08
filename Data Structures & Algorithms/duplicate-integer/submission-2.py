class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for element in nums:
            if element not in dict1:
                dict1[element] = 1
            else:
                dict1[element]+=1
        print(dict1)
        for key,value in dict1.items():
            if value > 1:
                return True
        return False


        