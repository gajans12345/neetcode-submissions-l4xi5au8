class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for element in s:
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            
            elif element == ')':
                if stack:
                    v = stack.pop()
                    if v == "(":
                        continue
                    else:
                        return False
                else:
                    return False
            elif element == ']':
                if stack:
                    v = stack.pop()
                    if v == "[":
                        continue
                    else:
                        return False
                else:
                    return False
            elif element == '}':
                if stack:
                    v = stack.pop()
                    if v == "{":
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True