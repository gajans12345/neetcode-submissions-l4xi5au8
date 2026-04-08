class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        found = 0
        curr_max = 0
        lst = []
        for element in nums:
            if element not in dict1.keys():
                dict1[element] = 1
            else:
                dict1[element]+=1
        print(dict1)
        for i in range(k):
            for element in dict1.keys():
                if dict1[element] > curr_max:
                    curr_max = dict1[element]
                    found = element
            dict1[found] = -1
            lst.append(found)
            curr_max = 0
        return lst
            


            
        