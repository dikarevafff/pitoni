'''
подключаемый файл с функциями, необходимыми для подсчёта символов в файле, нагрузки на пальцы
'''


def characters_in_file_counter(filename):
    '''
    получает: название файла
    возвращает: словарь "chars" - 'символ': количество
    '''
    
    #возвращаемый словарь: 'символ': количество
    chars = {}
    
    #заполнение словаря chars - анализ внешнего текстового
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            for char in line:
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
    return chars
 
def entry_checker(item, the_dict):
    '''
    получает: айтем, словарь
    возвращает: ключ, в значения которого входит айтем
    '''
    for key, value in the_dict.items():
        if item in value:
            return key


def finger_load_calculator(chars_dict, imported_layout, imported_scancodes_map):
    '''
    получает: словарь - 'символ': количество, файл со словарём разметки раскладки, файл со словарями соответствия сканкодов - цены/пальца
    возвращает: словарь "final_fingers_load" - 'палец': нагрузка
    '''

    #возвращаемый словарь 
    final_fingers_load = {
        'lfi2': 0,
        'lfi3': 0,
        'lfi4': 0,
        'lfi5': 0,
        'rfi2': 0,
        'rfi3': 0,
        'rfi4': 0,
        'rfi5': 0,
        'thumb': 0
    }

    #блок прогона каждой клавиши, поиск соответствия символа из словаря "chars" с файлом разметки раскладки, после сопоставления нагрузки и пальца
    for char, count in chars_dict.items():
        for key, value in imported_layout.layout_map.items():
            if char == key:
                if len(value) > 1: #если согласно файла разметки раскладки символ набирается с шифтом
                    scancode = value[1]
                    price = entry_checker(scancode, imported_scancodes_map.key_price)
                    finger = entry_checker(scancode, imported_scancodes_map.key_finger)
                    if not finger:
                        continue
                    final_fingers_load[finger] += count*price

                scancode = value[0]
                price = entry_checker(scancode, imported_scancodes_map.key_price)
                finger = entry_checker(scancode, imported_scancodes_map.key_finger)
                if not finger:
                        continue
                final_fingers_load[finger] += count*price
    return final_fingers_load