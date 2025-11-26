import random

data_list = random.sample(range(100), 10)

print("before ======= ", data_list)

for i in range(len(data_list) - 1):
    for j in range(i + 1, 0, -1):
        if data_list[j] < data_list[j - 1]:
            data_list[j], data_list[j - 1] = data_list[j - 1], data_list[j]

print("after ========= ", data_list)