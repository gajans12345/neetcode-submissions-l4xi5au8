from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        seenOne = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    seenOne = True
                if grid[i][j] == 2:
                    queue.append([i, j])

        if not queue and not seenOne:
            return 0

        minutes = 0
        while queue:
            temp = len(queue)
            for i in range(temp):
                currI, currJ = queue.popleft()
                if currI + 1 < m and grid[currI + 1][currJ] == 1:
                    grid[currI + 1][currJ] = 2
                    queue.append([currI + 1, currJ])
                if currI - 1 >= 0 and grid[currI - 1][currJ] == 1:
                    grid[currI - 1][currJ] = 2
                    queue.append([currI - 1, currJ])
                if currJ - 1 >= 0 and grid[currI][currJ - 1] == 1:
                    grid[currI][currJ - 1] = 2
                    queue.append([currI, currJ - 1])
                if currJ + 1 < n and grid[currI][currJ + 1] == 1:
                    grid[currI][currJ + 1] = 2
                    queue.append([currI, currJ + 1])
            minutes+=1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes - 1