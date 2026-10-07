class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = len(position)
        dict1 = {}
        for i in range(len(position)):
            dict1[position[i]] = speed[i]
        
        position = sorted(position,reverse=True)
        for i in range(len(position)):
            speed[i] = dict1[position[i]] 
        result = [0]*len(position)
        for i in range(len(position)):
            result[i] = float((target - position[i])/speed[i])
        stack = []
        #sorted [3,3,4.5,10]
        for element in result:
            if stack and element <= stack[-1][0]:
                stack[-1].append(element)
            else:
                stack.append([element])
        return len(stack)
        