# Задание 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# Задание 2

values_list = [1, 2.2, 'Urban']
print_params(*values_list)
values_dict = {'a': 5, 'b': False, 'c': 14.5}
print_params(**values_dict)

# Задание 3

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
