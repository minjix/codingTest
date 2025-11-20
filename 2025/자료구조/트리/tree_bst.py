class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head

        while True:
            if self.current_node.value > value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    

head = Node(1)
bst = NodeMgmt(head)
bst.search(2)
bst.search(3)
bst.search(5)

print(bst.search(1))
print(bst.search(4))
            
    