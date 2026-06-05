from collections import deque

class queue:
    def __init__(self):
        self.items = deque()

def enqueue(self, item):
    self.items.append(item)
    
def dequeue(self):
    if not self.is_empty():
        return self.items.popleft()
    return "queue kosong!"

def peek(self):
    if not self.if_empty():
        return self.items[0]
    
q = queue()
q.enqueue("Saipul")
q.enqueue("ahmad")
q.enqueue("anndi")

print(q)
print(q.peek())

print(q.dequeue())
print(q)
print(q.size())
print(q.is_empty())

