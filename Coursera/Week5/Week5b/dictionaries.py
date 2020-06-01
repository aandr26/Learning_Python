student = {'name': 'John', 'age': 25, 'courses' : ['Math', 'CompSci']}

student.update({'name' : 'Jane', 'age': 26, 'phone' : '555-5555'})


print(student)

del student['age']

print(student)