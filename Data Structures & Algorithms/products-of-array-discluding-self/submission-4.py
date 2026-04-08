class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]* len(nums)
        suffix = [0]* len(nums)
        lst = [0] * len(nums)
        prod = 1
        suff = 1
        for i in range(len(nums)):
            prefix[i] = prod
            prod *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suff
            suff*= nums[i]
        for i in range(len(nums)):
            lst[i] = prefix[i] * suffix[i]
        return lst

        