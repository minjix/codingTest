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

    # 추가
    def delete(self, data):
        
        if self.head == '':
            print("No Data")
            return

        node = self.head
        
        if self.head.data == data:    
            self.head = node.next
            del node
        else:
            while node.next:
                if node.next.data == data:
                    node_next = node.next
                    node.next = node.next.next
                    del node_next
                else:
                    node = node.next
        
linkedlist = NodeMgmt(0)
for i in range(1, 10):
    linkedlist.add(i)

linkedlist.delete(0)
linkedlist.delete(2)
linkedlist.delete(9)
linkedlist.desc()



