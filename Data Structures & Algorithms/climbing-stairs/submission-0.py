class Solution:
    def climbStairs(self, n: int) -> int:
        grid = [0] * (n + 1)
        if n == 2:
            return 2
        if n == 1:
            return 1
        grid[0] = 0
        grid[1] = 1
        grid[2] = 2
        for i in range(3,n+1):
            grid[i] = grid[i-1] + grid[i-2]
        return grid[n]
        