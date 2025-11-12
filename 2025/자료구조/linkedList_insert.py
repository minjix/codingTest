class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        node = self.head
        if node.data == '':
            node = Node(data)
        
        while node.next:
            node = node.next
        
        node.next = Node(data)


    def desc(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

linkedlist = NodeMgmt(0)
for i in range(1, 10):
    linkedlist.add(i)

linkedlist.desc() 