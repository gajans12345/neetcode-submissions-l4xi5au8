class Solution:
    def isValid(self, s: str) -> bool:
       # if len(s) % 2 != 0:
           # return False
        stack = []
        count = 0
        for element in s:
            if element == '(' or element == '{' or element == '[':
                stack.append(element)
            else:
                if element == ')':
                    if len(stack) > 0 and stack.pop(-1) == '(':
                        count+=1
                elif element =='}':
                    if len(stack) > 0 and stack.pop(-1) == '{':
                        count+=1
                elif element == ']':
                    if len(stack) > 0 and stack.pop(-1) == '[':
                        count+=1
        if count == len(s) / 2:
            return True
        else:
            return False