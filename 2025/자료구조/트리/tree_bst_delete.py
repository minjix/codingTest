import random

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
    
    # 삭제
    def delete(self, value):
        # 1. value 유무 검증
        searched = False
        self.current_node = self.head
        self.parent = self.head

        while self.current_node: 
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        if searched == False:
            return False              

        # 2. 삭제할 node가 leaf node일 때
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.current_node.value:
                self.parent.left = None
            else:    
                self.parent.right = None
            del self.current_node

        # 3. 삭제할 노드가 child node를 하나 가지고 있을 때
        # 3-1. child node가 왼쪽일 때
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.rigth = self.current_node.left
        # 3-1. child node가 오른쪽일 때
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.current_node.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        # 4. 삭제할 노드가 child node를 두개 가지고 있을 때(오른쪽 자식 중 가장 작은 값을 parent node가 가리기도록 함)
            if self.current_node.left != None and self.current_node.right != None:
        # 4-1. 삭제할 노드가 parent 왼쪽에 있을 때
                if value < self.parent.value:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
                    while self.change_node.left != None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                            
        # 4-1-1. 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 node의 child node가 없을 때
                    if self.change_node.right == None:
                        self.change_node_parent.left = None
                                        
        # 4-1-2. 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 node의 오른쪽에 child node가 있을 때        
                    else:
                        self.change_node_parent.left = self.change_node.right
                    
                    self.parent.left = self.change_node_parent
                    self.change_node.left = self.current_node.left
                    self.change_node.right = self.current_node.right
        # 4-2. 삭제할 노드가 parent 오른쪽에 있을 때
                else:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
                    while self.change_node.left != None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left

        # 4-2-1. 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 node의 child node가 없을 때
                    if self.change_node.right == None:
                        self.change_node_parent.left = None
        # 4-2-2. 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 node의 오른쪽에 child node가 있을 때       
                    else:
                        self.change_node_parent.left = self.change_node.right
                    self.parent = self.change_node
                    self.change_node.left = self.current_node.left
                    self.change_node.right = self.current_node.right
        
    

# 테스트 코드 작성
# 랜덤 함수 사용
#1. 0 ~999중 100개의 숫자 랜덤 선택
bst_num = set()
while len(bst_num) != 100:
    bst_num.add(random.randint(0, 999))
#2. 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
bst_tree = NodeMgmt(head)
for num in bst_num:
    bst_tree.insert(num)
#3. 입력한 100개의 숫자 검색(검색 기능 확인)
for num in bst_num:
    if bst_tree.search(num) == False:
        print('searched fail', num)
#4. 입력한 100개의 숫자 중 10개의 숫자 랜덤 선택
del_num = set()
bst_num = list(bst_num)
while len(del_num) != 10:
    del_num.add(bst_num[random.randint(0, 99)])
#5. 선택된 10개의 숫자를 삭제(삭제 기능 확인)
for num in del_num:
    if bst_tree.delete(num) == False:
        print('deleted fail', num)