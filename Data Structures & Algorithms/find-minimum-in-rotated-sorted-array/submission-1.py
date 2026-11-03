class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + ((r-l)//2)
            prevL = l
            prevR = r
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
                return nums[0]
        return nums[l]
        