class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        count = 0
        currIndex = 0
        k = 0
        copy = []
        if len(piles) == 0:
            return 0
        r = max(piles) + 1
        l = 1
        while l < r:
            count = 0
            k = (l + r) // 2  # find mid for binary search
            for element in piles:
                count += math.ceil(element / k)
            if count <= h:
                r = k
            else:
                l = k + 1

        return l  # (point where it converges is best)