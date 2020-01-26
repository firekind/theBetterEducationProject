class Stack:
    def __init__(self, size: int):
        self.elems = [None] * size
        self.size = size
        self.top = -1

    def push(self, elem: int) -> None:
        if self.top == len(self.elems) - 1:
            raise Exception("Stack overflow")
        
        self.top += 1
        self.elems[self.top] = elem
    
    def pop(self) -> int:
        if self.top < 0:
            raise Exception("Stack underflow")
        
        res = self.elems[self.top]
        self.elems[self.top] = None
        self.top -= 1
        return res

    def __str__(self) -> str:
        return ','.join(list(map(str, self.elems)))

s = Stack(size=3)
print(s)
s.push(0)
print(s)
s.push(1)
print(s)
s.push(2)
print(s)
# s.push(3)

s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
# s.pop()
