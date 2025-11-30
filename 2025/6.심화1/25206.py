grade = []
score = []
score_table = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

for _ in range(20):
    a, b, c = input().split()
    if c == "P":
        continue
    grade.append(float(b))
    score.append(score_table[c])

score_sum = 0.0

for i in range(len(score)):
    score_sum += (grade[i] * score[i])

print(score_sum / sum(grade))
