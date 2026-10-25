class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)        # rows
        n = len(heights[0])     # cols
        pacificArr = []
        atlanticArr = []
        resultPacific = {}      # cells that can drain into the Pacific
        resultAtlantic = {}     # cells that can drain into the Atlantic
        for j in range(n):
            pacificArr.append([0, j])        # top row
            atlanticArr.append([m - 1, j])   # bottom row
        for i in range(m):
            pacificArr.append([i, 0])        # left column
            atlanticArr.append([i, n - 1])   # right column

        def dfs(i, j, result):
            if (i, j) in result:
                return
            result[(i, j)] = 0
            # move UPHILL: neighbour must be >= current
            if i + 1 < m and heights[i + 1][j] >= heights[i][j]:
                dfs(i + 1, j, result)
            if i - 1 >= 0 and heights[i - 1][j] >= heights[i][j]:
                dfs(i - 1, j, result)
            if j + 1 < n and heights[i][j + 1] >= heights[i][j]:
                dfs(i, j + 1, result)
            if j - 1 >= 0 and heights[i][j - 1] >= heights[i][j]:
                dfs(i, j - 1, result)

        for element in pacificArr:
            dfs(element[0], element[1], resultPacific)
        for element in atlanticArr:
            dfs(element[0], element[1], resultAtlantic)

        result = []
        for cell in resultAtlantic:
            if cell in resultPacific:
                result.append([cell[0], cell[1]])
        return result