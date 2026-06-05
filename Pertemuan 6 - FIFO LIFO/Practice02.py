class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "stack kocong!"
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)


print(s)
print(s.pop())
print(s)
print(s.peek())
print(s)
print(s.is_empty())
print(s.size()) 
print(s)
print(s.pop())
