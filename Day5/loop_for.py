# fruit = ["Apple", "peach", "peat"]
# for i in fruit:
#     print(i)
# sum  len

studentList = input("Input a list of height student").split()
for n in range(0, len(studentList)):
    studentList[n] = int(studentList[n])
# sum = 0
# len = 0
# for i in studentList:
#     len += 1
#     sum += int(i)
# print(f"average height is {sum / len}")

# max min
maxScore = 0
for i in studentList:
    if i > maxScore:
        maxScore = i
print(f"heightest score is : {maxScore}")
