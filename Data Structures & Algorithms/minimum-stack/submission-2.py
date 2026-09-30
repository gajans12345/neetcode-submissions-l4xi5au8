class MinStack:

    def __init__(self): # IMplement using an array top is end of LL front
        self.stack = []
        self.lst = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.lst.append(val)

    def pop(self) -> None:
        del self.stack[-1]
        del self.lst[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        curMin = self.lst[0]
        for element in self.lst:
            if element < curMin:
                curMin = element
        return curMin
        
