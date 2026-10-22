class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIsles = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    stack = [[i, j]]
                    grid[i][j] = "0"          # mark when added
                    while stack:
                        currI, currJ = stack.pop()
                        if currI + 1 < m and grid[currI + 1][currJ] == "1":
                            grid[currI + 1][currJ] = "0"
                            stack.append([currI + 1, currJ])
                        if currI - 1 >= 0 and grid[currI - 1][currJ] == "1":
                            grid[currI - 1][currJ] = "0"
                            stack.append([currI - 1, currJ])
                        if currJ - 1 >= 0 and grid[currI][currJ - 1] == "1":
                            grid[currI][currJ - 1] = "0"
                            stack.append([currI, currJ - 1])
                        if currJ + 1 < n and grid[currI][currJ + 1] == "1":
                            grid[currI][currJ + 1] = "0"
                            stack.append([currI, currJ + 1])
                    numIsles += 1
        return numIsles