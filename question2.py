# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
student_mark=int(input("Enter the student mark in percentage:"))
if student_mark >=90:
    print("Grade A")
elif student_mark >=80:
    print("Grade B")
elif student_mark >=70:
    print("Grade C")
elif student_mark >=60:
    print("Grade D")
elif student_mark >=40:
    print("Grade E")
else:
    print("Grade F")