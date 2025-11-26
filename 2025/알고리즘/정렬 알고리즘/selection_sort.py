import random

data_list = random.sample(range(100), 10)

print("before ======= ", data_list)

for stand in range(len(data_list)-1):
    lowest = stand

    for i in range(stand + 1, len(data_list)):
        if data_list[lowest] > data_list[i]:
            lowest = i

    data_list[lowest], data_list[stand] = data_list[stand], data_list[lowest]

print("after ========= ", data_list)