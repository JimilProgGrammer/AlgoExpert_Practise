class MinMaxStack:
    self.minMaxStack = []
    self.stack = []
    
    # Time: O(1) | Space: O(1)
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    # Time: O(1) | Space: O(1)
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
    
    # Time: O(1) | Space: O(1)
    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
    
    # Time: O(1) | Space: O(1)
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["min"]
    
    # Time: O(1) | Space: O(1)
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["max"]
