grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_m = []
for num in grades:
    GPA = sum(num)/len(num)
    grades_m.append(GPA)
print(grades_m)
students_sort = sorted(students)
print(students_sort)
dict = dict(zip(students_sort, grades_m))
print(dict)