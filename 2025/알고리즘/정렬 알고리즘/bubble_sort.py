import random

#data_list = random.sample(range(100), 10)
data_list = [0,1,2,3,4,5,6,7,8,9]
print("before ======= ", data_list)

swap = False

for i in range(len(data_list)-1):
    for j in range(i + 1, len(data_list)):
        if data_list[i] > data_list[j]:
            data_list[i], data_list[j] = data_list[j], data_list[i]
            swap = True
    
        if swap == False:
            break

print("after ========= ", data_list)