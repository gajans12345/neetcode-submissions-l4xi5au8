class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dit = {}
        visited = set()
        for element in nums:
            dit[element] = []
        if len(nums) == 0:
            return 0
        streak = 1
        max1 = 0
        for key in dit:
            streak = 1
            if key in visited:
                continue
            visited.add(key)
            a = key - 1
            while a in dit and a not in visited:
                visited.add(a)
                streak += 1
                a -= 1
            b = key + 1
            while b in dit and b not in visited:
                visited.add(b)
                streak += 1
                b += 1


            if streak > max1:
                max1 = streak
        return max1

            
            
        