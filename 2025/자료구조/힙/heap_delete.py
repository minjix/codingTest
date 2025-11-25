class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        
        # 위치 변경 여부 확인
        if inserted_idx <= 1:
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def move_down(self, pop_index):
        
        # 삭제 시 위치 변경 여부 확인
        left_pop_idx = pop_index * 2
        right_pop_idx = pop_index * 2 + 1
        
        # 1. 자식노드의 맨 왼쪽 노드가 없는경우
        if left_pop_idx >= len(self.heap_array):
            return False
        # 2. 자식노드의 맨 왼쪽 노드O, 오른쪽이 없는 경우
        elif right_pop_idx >= len(self.heap_array):
            if self.heap_array[pop_index] < self.heap_array[left_pop_idx]:
                return True
            else:
                return False         

        # 3. 자식노드가 둘 다 있는 경우
        else:
            if self.heap_array[left_pop_idx] > self.heap_array[right_pop_idx]:
                if self.heap_array[pop_index] < self.heap_array[left_pop_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[pop_index] < self.heap_array[right_pop_idx]:
                    return True
                else:
                    return False

    def insert(self, data):
        # 1. 배열에 데이터 넣기
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) -1

        # 2. 데이터 위치 기반 체크 후 swap
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        
        return True

    def pop(self):
        # 1. 맨 위 루트 노드 삭제
        if len(self.heap_array) <= 1 :
            return None
        
        self.returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        pop_index = 1
        
        # 2. 트리 재구성
        while self.move_down(pop_index):
            left_pop_idx = pop_index * 2
            right_pop_idx = pop_index * 2 + 1
            
            # 2. 자식노드의 맨 왼쪽 노드O, 오른쪽이 없는 경우
            if right_pop_idx >= len(self.heap_array):
                if self.heap_array[pop_index] < self.heap_array[left_pop_idx]:
                    self.heap_array[pop_index], self.heap_array[left_pop_idx] = self.heap_array[left_pop_idx], self.heap_array[pop_index]
                    pop_index = left_pop_idx

            # 3. 자식노드가 둘 다 있는 경우
            else:
                if self.heap_array[left_pop_idx] > self.heap_array[right_pop_idx]:
                    if self.heap_array[pop_index] < self.heap_array[left_pop_idx]:
                        self.heap_array[pop_index], self.heap_array[left_pop_idx] = self.heap_array[left_pop_idx], self.heap_array[pop_index]
                        pop_index = left_pop_idx
                else:
                    if self.heap_array[pop_index] < self.heap_array[right_pop_idx]:
                        self.heap_array[pop_index], self.heap_array[right_pop_idx] = self.heap_array[right_pop_idx], self.heap_array[pop_index]
                        pop_index = right_pop_idx

        return self.returned_data
    
heap = Heap(15)
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
#heap.pop()
print(heap.pop())
print(heap.heap_array)