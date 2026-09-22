class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=0
        temp=[]
        while right < len(nums):
            if nums[right] != nums[left]:
                temp.append(nums[left])
                left = right
                right+=1
            else:
                right+=1
        left = len(nums) -1
        temp.append(nums[left])
        nums[:]=temp
        return len(nums)
        