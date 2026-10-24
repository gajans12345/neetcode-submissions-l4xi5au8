from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        if node.neighbors == []:
            v = Node(node.val, [])
            return v
        queue = deque()
        hashH = {}
        key = node.val
        queue.append(node)
        while queue:
            analyze = queue.popleft()
            arr = []
            if analyze.val not in hashH:
                hashH[analyze.val] = Node(analyze.val)
            for element in analyze.neighbors:
                if element.val not in hashH:
                    hashH[element.val] = Node(element.val)
                    queue.append(element)
                arr.append(hashH[element.val])
            hashH[analyze.val].neighbors = arr
        return hashH[key]