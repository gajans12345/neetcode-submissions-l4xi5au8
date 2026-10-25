class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        curr = []
        def helper(curr):
            for num in nums:
                if len(curr) == len(nums):
                    return
                else:
                    if num not in curr:
                        curr.append(num)
                        result.append(curr[:])
                        helper(curr)
                        curr.pop()
                    else:
                        return
        helper(curr)
        return result
        