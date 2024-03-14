import json


def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('operations.json', 'r', encoding='utf-8') as json_data_cart:
        data_cart = json.load(json_data_cart)
        return data_cart



def get_last_five_operations(data_cart):
    """Функция проверяет есть date в операциях и сортирует список операций по дате и возвращает 5 последних"""
    suitable_file = True
    n = 0
    for operations in data_cart:
        if 'date' not in operations:
            n += 1
            suitable_file = False
            break
    if suitable_file == True:
        data_cart.sort(key=lambda dictionary: dictionary['date'])
        return data_cart[-5:]
    else:
        return f"Отсутствует дата в операции номер - {n}"


def format_date(data: list):

    for el in data:
        date = el["date"].split('T')
        numbers = date[0].split('-')
        el["date"] = '.'.join(numbers)
        changed_pos = el['date'].split('.')
        el['date'] = '.'.join([changed_pos[2], changed_pos[1], changed_pos[0]])

    return data


def add_from_in_operations(last_five_operations_cart):
    """Функция проверян наличее срета отправителя и обавляет ключ from и значение 'Отсутствует' если такого ключа нет"""
    for operations in last_five_operations_cart:
        if len(operations) == 6:
            operations["from"] = "Отсутствует"
    return last_five_operations_cart


def disguise_sender_account(last_five_operations_cart):
    """Функция маскерует номер счета отправителя отображая первые 6 цифр и последние 4 цифры"""
    for operations in last_five_operations_cart:
        if operations["from"][0] == "M" or operations["from"][0] == "V":
            operations["from"] = operations["from"][:-12] + " " + operations["from"][-11:-9] + "*" * 2 + " " + "*" * 4 +\
                                 " " + operations["from"][-4:]

    return last_five_operations_cart


def disguise_recipients_account(last_five_operations_cart):
    """Функция маскерует номер счета получателя отображая только последние 4 цифры"""
    for operations in last_five_operations_cart:
        list_operations_to = operations["to"].split()
        cart = " ".join(list_operations_to[:-1])
        check = " ".join(list_operations_to[-1:])
        if operations["to"][4] == " ":
            operations["to"] = cart + " ** " + check[-4:]
        if operations["from"][4] == " ":
            operations["from"] = cart + " ** " + check[-4:]
    return last_five_operations_cart