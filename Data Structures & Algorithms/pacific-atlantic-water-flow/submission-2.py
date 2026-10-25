class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)        # rows
        n = len(heights[0])     # cols
        resultAtlantic = {}
        resultPacific = {}
        dict1 = {}              # current path (Atlantic)
        dict2 = {}              # current path (Pacific)

        def dfsAtlantic(i, j):
            if (i, j) in dict1:
                if (i,j) not in resultAtlantic:
                    return False
                return True
            dict1[(i, j)] = 0
            if i == m - 1 or j == n - 1:
                resultAtlantic[(i, j)] = 0
                return True

            down = up = right = left = False
            if i + 1 < m and heights[i][j] >= heights[i + 1][j]:
                down = dfsAtlantic(i + 1, j)
            if i - 1 >= 0 and heights[i][j] >= heights[i - 1][j]:
                up = dfsAtlantic(i - 1, j)
            if j + 1 < n and heights[i][j] >= heights[i][j + 1]:
                right = dfsAtlantic(i, j + 1)
            if j - 1 >= 0 and heights[i][j] >= heights[i][j - 1]:
                left = dfsAtlantic(i, j - 1)
            if not down and not right and not left and not up:
                return False
            if down or up or left or right:
                resultAtlantic[(i, j)] = 0
                return True

        def dfsPacific(i, j):
            if (i, j) in dict2:
                if (i,j) not in resultPacific:
                    return False
                return True
            dict2[(i, j)] = 0
            if i == 0 or j == 0:
                resultPacific[(i, j)] = 0
                return True

            down = up = right = left = False
            if i + 1 < m and heights[i][j] >= heights[i + 1][j]:
                down = dfsPacific(i + 1, j)
            if i - 1 >= 0 and heights[i][j] >= heights[i - 1][j]:
                up = dfsPacific(i - 1, j)
            if j + 1 < n and heights[i][j] >= heights[i][j + 1]:
                right = dfsPacific(i, j + 1)
            if j - 1 >= 0 and heights[i][j] >= heights[i][j - 1]:
                left = dfsPacific(i, j - 1)
            if not down and not right and not left and not up:
                return False
            if down or up or left or right:
                resultPacific[(i, j)] = 0
                return True

        for i in range(m):
            for j in range(n):
                # TODO: call both dfs? store results?
                dict1.clear()
                dfsAtlantic(i, j)
                dict2.clear()
                dfsPacific(i, j)

        result = []
        for cell in resultAtlantic:
            if cell in resultPacific:
                result.append([cell[0], cell[1]])
        return result