class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = []
        for i in range(numCourses):
            graph.append([])                      # was: [0] * numCourses
        for element in prerequisites:
            graph[element[0]].append(element[1])  # was: grid[a][b] = 1

        globalMap = {}
        innerH = {}

        def dfs(start):
            if start in innerH:
                return False
            if start in globalMap:
                return True
            innerH[start] = 0
            for i in graph[start]:                # was: scan row, check == 1
                if not dfs(i):
                    return False
            globalMap[start] = 0
            del innerH[start]
            return True

        for i in range(numCourses):
            if i in globalMap:
                continue
            if not dfs(i):
                return False
        return True