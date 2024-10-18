# Домашнее задание по теме "Интроспекция"
from pprint import pprint
import sys

# Создайте функцию introspection_info(obj), которая принимает объект obj.
def introspection_info(obj):
    # Верните словарь или строки с данными об объекте, включающий следующую информацию:
    #  - Тип объекта.
    #  - Атрибуты объекта.
    #  - Методы объекта.
    #  - Модуль, к которому объект принадлежит.
    #  - Другие интересные свойства объекта, учитывая его тип (по желанию)
    dict = {}
    dict['os'] = str(sys.platform)
    dict['type'] = type(obj).__name__
    dict['attributes'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    dict['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    dict['module'] = introspection_info.__module__
    return (dict)

number_info = introspection_info(42)
pprint(number_info)
