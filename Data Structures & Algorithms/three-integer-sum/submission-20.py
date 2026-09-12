class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        set1 = set()
        results = []
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)):
            compliment = -1 * nums[i]
            l = i + 1
            while l<r:
                if nums[r] + nums[l] == compliment:
                    lst = tuple(sorted([nums[i], nums[l], nums[r]]))
                    set1.add(lst)
                    l+=1
                    r-=1
                else:
                    if nums[r] + nums[l] > compliment:
                        r-=1
                    else:
                        l+=1
            r = len(nums)-1
        for element in set1:
            results.append(list(element))
        return results

                    
                    
