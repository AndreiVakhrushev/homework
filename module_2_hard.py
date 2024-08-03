def code(numbers):
    result = []
    for i in range(1, numbers + 1):
        for j in range(i + 1, numbers + 1):
            sum = i + j
            if numbers % sum == 0:
                result.append(i)
                result.append(j)
    return result
numbers = int(input('Число из первой вставки: '))
result = code(numbers)
print('Нужный пароль - ',*result, sep='')
