class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            new.prev = node
            node.next = new
            self.tail = new

    def search_from_head(self, data):
        if self.head == None:
            print("No data")
            return
        else:
            node = self.head
            while node:
                if node.data == data:
                    print(node.data)
                    return
                else:
                    node = node.next
            return False

    def search_from_tail(self, data):
        if self.head == None:
            print("No data")
            return
        else:
            node = self.tail
            while node:
                if node.data == data:
                    print(node.data)
                    return
                else:
                    node = node.prev
            return False

    def desc(self):
        if self.head == None:
            print("No data")
            return
        else:
            node = self.head
            while node:
                print(node.data)
                node = node.next

    def insert_before(self, data, bf_data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return True
        else:
            node = self.tail
            while node:
                if node.data == bf_data:
                    new = Node(data)
                    before_new = node

                    new.next = before_new
                    new.prev = before_new.prev
                    before_new.prev.next = new
                    before_new.prev = new
                    return True
                else:
                    node = node.prev
    
    def insert_after(self, data, af_data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return True
        else:
            node = self.tail
            while node:
                if node.data == af_data:
                    new = Node(data)
                    after_new = node

                    new.next = after_new.next
                    new.prev = after_new.next
                    after_new.next.prev = new
                    after_new.next = new
                    return True
                else:
                    node = node.prev

ll = NodeMgmt(0)

for i in range(1,10):
    ll.insert(i)

#ll.desc()

ll.insert_before(1.5,2)
ll.desc()

print("===========================")

ll.insert_after(3.5,3)
ll.desc()