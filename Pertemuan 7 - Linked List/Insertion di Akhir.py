class node:
    def __init__(self, data):
        self.data = data
        self.next = None    

def insert_at_end(head, data):
    new_node = node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

head = None
head = insert_at_end(head, "A")
head = insert_at_end(head, "B")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] -> ", end="")
        head = head.next
    print("NULL")


print_linked_list(head)