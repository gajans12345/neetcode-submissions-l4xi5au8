class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array of integers where index i is temp on ith day
        # return a result where result i is number of days after ith day where we find a warmer temp else 0
        # edge cases : assume array and atleast 2 elements
        #  no circle wrapping
        # strictly greater
        # hahsmpas, 2 pointer ,sliding windows or stacks and queues
        #
        result = [0] * len(temperatures)
        stack = [0] # holding stuff to find  a temp
        for i in range(1,len(temperatures)):
            if temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)


            

        return result
                
            