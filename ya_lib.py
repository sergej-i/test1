from random import randint

max_diff_items = 100 # пусть имён будет конечное небольшое число
max_items_count = 50 # ограничим максимальное число генерируемых словарей
max_item_val = 1000000 # пусть значения элементов в словарях также ограничены сверху

zeros = len(str(max_diff_items)) # чтобы имена были красивые...

def gen_name_by_i(i):
    return 'key_' + f'{randint(0, i + 1):0>{zeros}}'

def gen_val():
    return randint(1, max_item_val)
