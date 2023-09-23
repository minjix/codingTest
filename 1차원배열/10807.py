n = int(input())
l = list(map(int, input().split()))
v = int(input())

print(l.count(v)) #count(값) : 같은 값을 찾아주는 메서드

#내장 함수 사용하지 않는 방법
# count = 0
# for i in l:
#     if i == V:
#         count += 1