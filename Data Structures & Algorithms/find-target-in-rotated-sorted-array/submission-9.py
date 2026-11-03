class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        left = 0
        right = 0
        while l < r:
            mid = l + ((r-l)//2)
            if nums[mid] > nums[r]:
                if l == mid:
                    l = mid + 1
                else:
                    l = mid 
            elif nums[mid] < nums[l]:
                if r == mid:
                    r = mid - 1
                else:
                    r = mid 
            else:
                break
        if nums[l] == target:
            return l
        if l == 0:
            left = 0
            right = len(nums) - 1
        elif target < nums[0]:
            left = l+1
            right = len(nums) - 1
        else:
            left = 0
            right = l - 1
        while left <= right:
            mid = left + ((right-left)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return - 1



