import random

def qsort(data):
    if len(data) <= 1:
        return data
    
    left,right = list(), list()

    pivot = data[0]

    for i in range(1, len(data)):
        if data[i] < pivot:
            left.append(data[i])
        else:
            right.append(data[i])
    
    return qsort(left) + [pivot] + qsort(right)

def qsort_comprehension(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]

    return qsort_comprehension(left) + [pivot] + qsort_comprehension(right)

data_list = random.sample(range(100), 10)
print(qsort(data_list))
print(qsort_comprehension(data_list))