from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dict1 = {}
        tempList = wordList
        tempList.append(beginWord)
        length = len(beginWord)
        for i in range(len(tempList)):
            dict1[tempList[i]] = []
            for j in range(len(tempList)):
                if i != j:
                    count = 0
                    for k in range(length):
                        if tempList[i][k] == tempList[j][k]:
                            count += 1
                    if count == length - 1:
                        dict1[tempList[i]].append(tempList[j])
        if endWord not in dict1 or dict1[beginWord] == [] or dict1[endWord] == []:
            return 0

        visited = {}
        queue = deque([beginWord])
        count = 1
        while queue:
            t = len(queue)
            for i in range(t):
                node = queue.popleft()
                for word in dict1[node]:
                    if word not in visited:
                        visited[word] = 0
                        queue.append(word)
                    if word == endWord:
                        return count + 1
            count += 1
        return 0