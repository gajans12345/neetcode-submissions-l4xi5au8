class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        dict1 = set()
        nums.sort()
        for i in range(len(nums)):
            a = i+1
            b = len(nums) - 1
            while a < b:
                if nums[i] + nums[a] + nums[b] == 0:
                    dict1.add((nums[i], nums[a], nums[b]))
                    a = a + 1
                    b = b - 1
                elif nums[i] + nums[a] + nums[b] >0:
                    b -= 1
                elif nums[i] + nums[a] + nums[b] < 0:
                    a = a + 1
                 
        return [list(triplet) for triplet in dict1 ]

            
        
        