class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        lst = [[] for _ in range(len(nums) + 1)]
        v = []
        print(lst)
        for i in range(len(nums)):
            if nums[i] not in dict1.keys():
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] +=1
        for element in dict1.keys():
            lst[dict1[element]].append(element)
        
        for i in range(len(nums),0,-1):
            for element in lst[i]:
                if len(v) == k:
                    break
                else:
                    if len(lst[i])!=0:
                        v.append(element)
        return v





        

            
        