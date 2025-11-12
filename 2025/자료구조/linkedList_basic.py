class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

for i in range(3,11):
    add(i)

# 중간 삽입 추가
node = head
node3 = Node(1.5)

search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

while node.next:
    print(node.data)
    node = node.next

    


