my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
i = 0
while i<len(my_list):
    if my_list[i] > a:
        print(my_list[i])
    if my_list[i] < 0:
        break
    i += 1
