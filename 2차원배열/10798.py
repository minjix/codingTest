# 다시 해보기!!
string = []

for row in range(5):
    row = input()
    string.append(row)
# string = [input() for i in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(string[j]):
            print(string[j][i], end="")

