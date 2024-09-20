
def apply_all_func(int_list, *functions):
    resalts = {}
    for function in functions:
        resalts[function.__name__] = function(int_list)
    return resalts


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
