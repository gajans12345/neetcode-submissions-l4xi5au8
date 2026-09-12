class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            compliment = -1 * nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[r] + nums[l] == compliment:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    if nums[r] + nums[l] > compliment:
                        r -= 1
                    else:
                        l += 1
        return results