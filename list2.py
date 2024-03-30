class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SLlist:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert(self, x):
        x.next = self.head
        self.head = x
        self.size += 1
    
    def delete(self, x):
        n = x.next
        if n is not None:
            x.next = n.next
            n = None
            self.size -= 1
    
    def search(self, k):
        x = self.head
        while x is not None and x.data == k:
            x = x.next
        return x

    def get(self, id):
        x = self.head
        for i in range(id+1):
            x = x.next
        return x
    

        