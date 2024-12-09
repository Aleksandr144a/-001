grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)
students_and_grades = {}

for index in range(len(sorted_students)):
    student = sorted_students[index]
    student_grades = grades[index]
    grade = sum(student_grades) / len(student_grades)
    students_and_grades[student] = grade

print(students_and_grades)
