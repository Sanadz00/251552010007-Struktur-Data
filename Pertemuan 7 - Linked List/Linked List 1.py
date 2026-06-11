class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node("15")
b = Node("16")
c = Node("17")
d = Node("18")

a.next = b
b.next = c
c.next = d

current = a
while current:
    print(f"Node @ {id(current)} |Data:{current.data} |Next:{id(current.next) if current.next else None}")
    current = current.next