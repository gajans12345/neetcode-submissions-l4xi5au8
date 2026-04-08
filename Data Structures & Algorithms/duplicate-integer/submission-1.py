class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for number in nums:
            if number not in dict:
                dict[number] = 0
            else:
                return True
        return False

        