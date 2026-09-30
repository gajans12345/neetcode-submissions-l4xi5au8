class MinStack:

    def __init__(self): # IMplement using an array top is end of LL front
        self.stack = []
        self.minCalc = []

        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minCalc.append(val)
        else:
            self.stack.append(val)
            if val < self.minCalc[-1]:
                self.minCalc.append(val)
            else:
                self.minCalc.append(self.minCalc[-1])  

    def pop(self) -> None:
        del self.stack[-1]
        del self.minCalc[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minCalc[-1]
        
