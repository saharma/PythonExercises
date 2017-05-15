grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(grades.count(7))
grades[len(grades)-1] = 4
print(max(grades))
grades.sort()
print(sum(grades)/float(len(grades)))