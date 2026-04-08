class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            m = target - nums[i]
            if(m in myDict):
                return [myDict[m],i]
            else:
                myDict[nums[i]] = i

        