class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        
        while right < len(nums):
            if nums[right] != nums[left]:
                print(left,nums[left],"if")
                left = right
                right+=1
            else:
                del nums[right]
        return len(nums)
        