class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        count = 0
        for element in s:
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            else:
                if element == ')':
                    if len(stack) > 0 and stack.pop() == '(':
                        count+=1
                    else:
                        return False
                elif element == ']':
                    if len(stack) > 0 and stack.pop() == '[':
                        count+=1
                    else:
                        return False
                elif element == '}':
                    if len(stack) > 0 and stack.pop() == '{':
                        count+=1
                    else:
                        return False
        if count == len(s) / 2:
            return True
        else:
            return False