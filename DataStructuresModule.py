class Stack:
    def __init__(self, stack_size):
        self.stack = [None] * stack_size
        self.cursor = -1
    
    def push(self, item):
        if (self.cursor < len(self.stack) - 1):
            self.cursor = self.cursor + 1
            self.stack[self.cursor] = item
        else:
            print("Stack full.  Cannot add elements")
    
    def pop(self):
        if (self.cursor == -1):
            print("No items in stack")
        else:
            item = self.stack[self.cursor]
            self.stack[self.cursor] = None
            self.cursor = self.cursor - 1
            return item

    def printLength(self):
        return (len(self.stack))

    def print(self):
        print('Base-->', end = '')
        for i in range(0, self.cursor + 1):
            print (self.stack[i], end = ' ')
        print('<--Top')


def createStack(size):
    return Stack(size)