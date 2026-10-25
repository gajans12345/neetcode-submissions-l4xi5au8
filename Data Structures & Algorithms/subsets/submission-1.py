class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        curr = []
        def helper(curr,start):
            for i in range(start,len(nums)):
                if len(curr) == len(nums):
                    return
                else:
                    curr.append(nums[i])
                    result.append(curr[:])
                    helper(curr,i+1)
                    curr.pop()
        helper(curr,0)
        return result
        