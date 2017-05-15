name = input("Enter name: ")
student_number = input("Enter student number: ")

ask = True
subjects = []
while ask:
	subject = input("Enter subject. Enter 'done' when finished: ")
	if subject == "done":
		ask = False
		break
	subjects.append(subject)

print(name)
print(student_number)
print(subjects)			
