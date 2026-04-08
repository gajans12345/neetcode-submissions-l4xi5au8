class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # edge cases
        if len(nums) == 0:
            return 0
        lst = []
        dict1 = {}
        for element in nums:
            if element in dict1:
                dict1[element]+=1
            else:
                dict1[element] = 1
        
        for i in range(k):
            curMax = 0
            delkey = 0
            for key,value in dict1.items():
                if value > curMax:
                    curMax = value
                    delkey = key
            del dict1[delkey]
            lst.append(delkey)
        return lst
            

        


        