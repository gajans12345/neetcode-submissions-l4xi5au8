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
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for x,y in dict1.items():
            freq[y].append(x)
        
        for i in range(len(freq)-1,0,-1):
            print(i)
            for element in freq[i]:
                lst.append(element)
                if len(lst) == k:
                    return lst
            


            
        