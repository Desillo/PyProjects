
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None

class Llist:
    def __init__(self, *nodes) -> None:
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil
        if nodes:
            for n in nodes:
                self.insert(Node(n))

    
    def search(self, k):
        x = self.nil.next
        while x is not self.nil and x.data != k:
            x = x.next
        return x


    def insert(self, x):
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil
        
    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
    
    def PrintLL(self):
        node = self.nil.prev
        while node.data != None:
            print(str(node.next.data) + " -> " + str(node.data) + " -> " + str(node.prev.data))
            node = node.prev
L = [1,2,3,4,5]
Ll = Llist()
Ll.PrintLL()

