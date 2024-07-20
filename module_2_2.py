first = input('Введите первое значение: ')
print(first)
second = input('Введите второе значение: ')
print(second)
third = input('Введите третье число: ')
print(third)
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
