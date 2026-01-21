#Write a program to input marks of a student and display the grade using if-elif-else.

marks = float(input("Enter the marks obtained by the student: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'

print("The grade of the student is:", grade)