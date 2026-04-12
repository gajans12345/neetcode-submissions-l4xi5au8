class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums) * 2
        ans = [0] * length
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans
