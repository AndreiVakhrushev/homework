immutable_var_1 = 1, 2, 'a', 'b'
immutable_var_2 = (1, 2, 'a', 'b')
immutable_var_3 = tuple ([1, 2, 'a', 'b'])
print(immutable_var_1)
print(immutable_var_2)
print(immutable_var_3)
# print(immutable_var_1[1]) = 4 (кортеж не поддерживает обращение по элементам)
mutable_list = [1, 2, 'a', 'b', 'Modified']
print(mutable_list)
mutable_list[0] = 'c'
print(mutable_list)
mutable_list[3] = 'Urban'
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend('Andrei')
print(mutable_list)
mutable_list.remove('Modified')
print(mutable_list)
print('Modified' in mutable_list)
print('Modified' not in mutable_list)
print(mutable_list[3:6])
print(mutable_list[0::2])