class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        lst = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict1:
                return [dict1[complement], i]
            dict1[nums[i]] = i
        